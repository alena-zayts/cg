.MODEL TINY

CODESEG SEGMENT
	ASSUME CS:CODESEG, DS:CODESEG
    ORG 100H					; 256 байт под PSP - Program Segment Prefix

MAIN:  
	JMP INSTALL					; при первом заходе устанавливаем
	SAVED9 DD ?					; старый вектор прерывания		
    FLAG    DB  '1'				; установлен или нет
	
NEW9 PROC
    PUSH AX						; сохраняем старые регистры и флаги
    PUSH BX
    PUSH CX
    PUSH DX
    PUSH ES
    PUSH DS
	PUSH DI  
	PUSH SI
    PUSHF

    CALL CS:SAVED9				; вызываем старый обработчик

    ; IN AX, 60H					; Порт 60h
								;доступен для записи и обычно принимает пары байтов последовательно: первый - код
								;команды, второй - данные. В частности, команда F3h отвечает за параметры режима
								;автоповтора нажатой клавиши.
    ; CMP AH, 243
    ; JNE EXIT					; если вызвана не команда F3h, больше ничего не делаем
;7 бит (старший) - всегда 0
;5,6 биты - пауза перед началом автоповтора (250, 500, 750 или 1000 мс)
;4-0 биты - скорость автоповтора (от 0000b (30 символов в секунду) до 11111b - 2
; ';символа в секунду).
	; MOV BL, AL
	; AND BL, 31
	; INC BL
	
	; AND AL, 96
	; OR AL, BL

    EXIT:						; восстанавливаем старые регистры и флаги
        POP DS
        POP ES
        POP DX
        POP CX
        POP BX
        POP AX
        IRET
NEW9 ENDP

INSTALL:						; установка
    MOV AX, 3509H 				; AH = 35H возвращает значение вектора прерывания для INT (AL); то есть, 
								; загружает в BX 0000:[AL*4], а в ES - 0000:[(AL*4)+2].
							
								;Прерывания, вызванные приходом кодов нажатия и отпускания клавиш, обрабатывает BIOS Int 9h. 
								;Результат обработки (как правило, ASCII-символ в младшем байте и скан-код в старшем) 
								;помещается в клавиатурный буфер, расположенный в ОЗУ. 
    INT 21H

    CMP ES:FLAG, '1'		    ; если уже установлено, разустанавливаем
    JE UNINSTALL

								; сохраняем старый обработчик прерывания
    MOV WORD PTR SAVED9, BX		
    MOV WORD PTR SAVED9 + 2, ES

    MOV AX, 2509H				; устанавливаем новый вектор прерывания
    LEA DX, NEW9 
    INT 21H

    LEA DX, INSTALL				; DX = адрес первого байта за резидентным участком программы (DX интерпретируется как смещение от PSP (DS/ES при запуске)
    INT 27H						; Эта функция завершает программу, оставляя резидентную часть (обработчик прерывания) в памяти.					

UNINSTALL:
    PUSH ES						; сохраняем ES и DS в стеке
    PUSH DS

    MOV DX, WORD PTR ES:SAVED9		
    MOV DS, WORD PTR ES:SAVED9 + 2
    MOV AX, 2509H
    INT 21H						; устанавливаем старый вектор прерывания

    POP DS						; возвращаем ES и DS из стека
    POP ES

    MOV AH, 49H					; Освобождает блок памяти, начинающийся с адреса ES:0000. этот блок становится доступным для других запросов системы.
    INT 21H						; ES = сегментный адрес (параграф) освобождаемого блока памяти


    MOV AX, 4C00H				; завершаем программу
    INT 21H
CODESEG ENDS
END MAIN