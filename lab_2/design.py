# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_root(object):
    def setupUi(self, root):
        root.setObjectName("root")
        root.resize(2500, 1400)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(root.sizePolicy().hasHeightForWidth())
        root.setSizePolicy(sizePolicy)
        root.setMinimumSize(QtCore.QSize(2500, 1400))
        root.setMaximumSize(QtCore.QSize(2500, 1400))
        self.centralwidget = QtWidgets.QWidget(root)
        self.centralwidget.setObjectName("centralwidget")
        self.lb_dy = QtWidgets.QLabel(self.centralwidget)
        self.lb_dy.setGeometry(QtCore.QRect(20, 190, 41, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lb_dy.setFont(font)
        self.lb_dy.setObjectName("lb_dy")
        self.lb_dx = QtWidgets.QLabel(self.centralwidget)
        self.lb_dx.setGeometry(QtCore.QRect(20, 130, 41, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_dx.sizePolicy().hasHeightForWidth())
        self.lb_dx.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lb_dx.setFont(font)
        self.lb_dx.setObjectName("lb_dx")
        self.en_dx = QtWidgets.QLineEdit(self.centralwidget)
        self.en_dx.setGeometry(QtCore.QRect(60, 130, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.en_dx.setFont(font)
        self.en_dx.setObjectName("en_dx")
        self.bt_shift = QtWidgets.QPushButton(self.centralwidget)
        self.bt_shift.setGeometry(QtCore.QRect(30, 260, 221, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bt_shift.setFont(font)
        self.bt_shift.setObjectName("bt_shift")
        self.graph = QtWidgets.QGraphicsView(self.centralwidget)
        self.graph.setGeometry(QtCore.QRect(320, 40, 2100, 1100))
        self.graph.setObjectName("graph")
        self.en_dy = QtWidgets.QLineEdit(self.centralwidget)
        self.en_dy.setGeometry(QtCore.QRect(60, 190, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.en_dy.setFont(font)
        self.en_dy.setObjectName("en_dy")
        self.bt_scale = QtWidgets.QPushButton(self.centralwidget)
        self.bt_scale.setGeometry(QtCore.QRect(20, 820, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bt_scale.setFont(font)
        self.bt_scale.setObjectName("bt_scale")
        self.lb_xm = QtWidgets.QLabel(self.centralwidget)
        self.lb_xm.setGeometry(QtCore.QRect(20, 480, 51, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_xm.sizePolicy().hasHeightForWidth())
        self.lb_xm.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lb_xm.setFont(font)
        self.lb_xm.setObjectName("lb_xm")
        self.en_xm = QtWidgets.QLineEdit(self.centralwidget)
        self.en_xm.setGeometry(QtCore.QRect(80, 480, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.en_xm.setFont(font)
        self.en_xm.setObjectName("en_xm")
        self.lb_ym = QtWidgets.QLabel(self.centralwidget)
        self.lb_ym.setGeometry(QtCore.QRect(20, 550, 51, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_ym.sizePolicy().hasHeightForWidth())
        self.lb_ym.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lb_ym.setFont(font)
        self.lb_ym.setObjectName("lb_ym")
        self.en_ym = QtWidgets.QLineEdit(self.centralwidget)
        self.en_ym.setGeometry(QtCore.QRect(80, 550, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.en_ym.setFont(font)
        self.en_ym.setObjectName("en_ym")
        self.lb_kx = QtWidgets.QLabel(self.centralwidget)
        self.lb_kx.setGeometry(QtCore.QRect(20, 680, 41, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_kx.sizePolicy().hasHeightForWidth())
        self.lb_kx.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lb_kx.setFont(font)
        self.lb_kx.setObjectName("lb_kx")
        self.en_kx = QtWidgets.QLineEdit(self.centralwidget)
        self.en_kx.setGeometry(QtCore.QRect(80, 680, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.en_kx.setFont(font)
        self.en_kx.setObjectName("en_kx")
        self.lb_ky = QtWidgets.QLabel(self.centralwidget)
        self.lb_ky.setGeometry(QtCore.QRect(20, 750, 41, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_ky.sizePolicy().hasHeightForWidth())
        self.lb_ky.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lb_ky.setFont(font)
        self.lb_ky.setObjectName("lb_ky")
        self.en_ky = QtWidgets.QLineEdit(self.centralwidget)
        self.en_ky.setGeometry(QtCore.QRect(80, 750, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.en_ky.setFont(font)
        self.en_ky.setObjectName("en_ky")
        self.en_yc = QtWidgets.QLineEdit(self.centralwidget)
        self.en_yc.setGeometry(QtCore.QRect(80, 1090, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.en_yc.setFont(font)
        self.en_yc.setObjectName("en_yc")
        self.lb_ym_2 = QtWidgets.QLabel(self.centralwidget)
        self.lb_ym_2.setGeometry(QtCore.QRect(20, 1100, 41, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_ym_2.sizePolicy().hasHeightForWidth())
        self.lb_ym_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lb_ym_2.setFont(font)
        self.lb_ym_2.setObjectName("lb_ym_2")
        self.en_teta = QtWidgets.QLineEdit(self.centralwidget)
        self.en_teta.setGeometry(QtCore.QRect(80, 1220, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.en_teta.setFont(font)
        self.en_teta.setObjectName("en_teta")
        self.lb_kx_2 = QtWidgets.QLabel(self.centralwidget)
        self.lb_kx_2.setGeometry(QtCore.QRect(20, 1230, 41, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_kx_2.sizePolicy().hasHeightForWidth())
        self.lb_kx_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lb_kx_2.setFont(font)
        self.lb_kx_2.setObjectName("lb_kx_2")
        self.bt_turn = QtWidgets.QPushButton(self.centralwidget)
        self.bt_turn.setGeometry(QtCore.QRect(30, 1310, 261, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bt_turn.setFont(font)
        self.bt_turn.setObjectName("bt_turn")
        self.lb_xm_2 = QtWidgets.QLabel(self.centralwidget)
        self.lb_xm_2.setGeometry(QtCore.QRect(20, 1020, 41, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_xm_2.sizePolicy().hasHeightForWidth())
        self.lb_xm_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lb_xm_2.setFont(font)
        self.lb_xm_2.setObjectName("lb_xm_2")
        self.en_xc = QtWidgets.QLineEdit(self.centralwidget)
        self.en_xc.setGeometry(QtCore.QRect(80, 1010, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.en_xc.setFont(font)
        self.en_xc.setObjectName("en_xc")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 281, 321))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 380, 291, 511))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 240, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 920, 291, 461))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.groupBox_3.setFont(font)
        self.groupBox_3.setObjectName("groupBox_3")
        self.label_5 = QtWidgets.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(10, 40, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(10, 240, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.bt_again = QtWidgets.QPushButton(self.centralwidget)
        self.bt_again.setGeometry(QtCore.QRect(370, 1160, 401, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bt_again.setFont(font)
        self.bt_again.setObjectName("bt_again")
        self.bt_back = QtWidgets.QPushButton(self.centralwidget)
        self.bt_back.setGeometry(QtCore.QRect(860, 1160, 211, 91))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.bt_back.setFont(font)
        self.bt_back.setObjectName("bt_back")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(1170, 1160, 291, 181))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.groupBox_4.setFont(font)
        self.groupBox_4.setObjectName("groupBox_4")
        self.lb_x0 = QtWidgets.QLabel(self.groupBox_4)
        self.lb_x0.setGeometry(QtCore.QRect(10, 40, 61, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_x0.sizePolicy().hasHeightForWidth())
        self.lb_x0.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lb_x0.setFont(font)
        self.lb_x0.setObjectName("lb_x0")
        self.en_x0 = QtWidgets.QLineEdit(self.groupBox_4)
        self.en_x0.setEnabled(False)
        self.en_x0.setGeometry(QtCore.QRect(90, 40, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.en_x0.setFont(font)
        self.en_x0.setObjectName("en_x0")
        self.lb_y0 = QtWidgets.QLabel(self.groupBox_4)
        self.lb_y0.setGeometry(QtCore.QRect(10, 120, 61, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lb_y0.sizePolicy().hasHeightForWidth())
        self.lb_y0.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.lb_y0.setFont(font)
        self.lb_y0.setObjectName("lb_y0")
        self.en_y0 = QtWidgets.QLineEdit(self.groupBox_4)
        self.en_y0.setEnabled(False)
        self.en_y0.setGeometry(QtCore.QRect(90, 120, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.en_y0.setFont(font)
        self.en_y0.setObjectName("en_y0")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(1480, 1160, 611, 151))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.groupBox.raise_()
        self.groupBox_3.raise_()
        self.groupBox_2.raise_()
        self.lb_dy.raise_()
        self.lb_dx.raise_()
        self.en_dx.raise_()
        self.bt_shift.raise_()
        self.graph.raise_()
        self.en_dy.raise_()
        self.bt_scale.raise_()
        self.lb_xm.raise_()
        self.en_xm.raise_()
        self.lb_ym.raise_()
        self.en_ym.raise_()
        self.lb_kx.raise_()
        self.en_kx.raise_()
        self.lb_ky.raise_()
        self.en_ky.raise_()
        self.en_yc.raise_()
        self.lb_ym_2.raise_()
        self.en_teta.raise_()
        self.lb_kx_2.raise_()
        self.bt_turn.raise_()
        self.lb_xm_2.raise_()
        self.en_xc.raise_()
        self.bt_again.raise_()
        self.bt_back.raise_()
        self.groupBox_4.raise_()
        self.label.raise_()
        root.setCentralWidget(self.centralwidget)

        self.retranslateUi(root)
        QtCore.QMetaObject.connectSlotsByName(root)

    def retranslateUi(self, root):
        _translate = QtCore.QCoreApplication.translate
        root.setWindowTitle(_translate("root", "Преобразования на плоскости"))
        self.lb_dy.setText(_translate("root", "dy:"))
        self.lb_dx.setText(_translate("root", "dx: "))
        self.en_dx.setText(_translate("root", "0"))
        self.bt_shift.setText(_translate("root", "Перенести"))
        self.en_dy.setText(_translate("root", "0"))
        self.bt_scale.setText(_translate("root", "Масштабировать"))
        self.lb_xm.setText(_translate("root", "xm:"))
        self.en_xm.setText(_translate("root", "0"))
        self.lb_ym.setText(_translate("root", "ym:"))
        self.en_ym.setText(_translate("root", "0"))
        self.lb_kx.setText(_translate("root", "kx:"))
        self.en_kx.setText(_translate("root", "1"))
        self.lb_ky.setText(_translate("root", "ky:"))
        self.en_ky.setText(_translate("root", "1"))
        self.en_yc.setText(_translate("root", "0"))
        self.lb_ym_2.setText(_translate("root", "yс:"))
        self.en_teta.setText(_translate("root", "0"))
        self.lb_kx_2.setText(_translate("root", "θ:"))
        self.bt_turn.setText(_translate("root", "Повернуть"))
        self.lb_xm_2.setText(_translate("root", "xс:"))
        self.en_xc.setText(_translate("root", "0"))
        self.groupBox.setTitle(_translate("root", "Перенос"))
        self.label_2.setText(_translate("root", "Величины смещения"))
        self.groupBox_2.setTitle(_translate("root", "Масштабирование"))
        self.label_3.setText(_translate("root", "Центр"))
        self.label_4.setText(_translate("root", "Коэффициенты"))
        self.groupBox_3.setTitle(_translate("root", "Поворот"))
        self.label_5.setText(_translate("root", "Центр"))
        self.label_6.setText(_translate("root", "Угол"))
        self.bt_again.setText(_translate("root", "Исходное изображение"))
        self.bt_back.setText(_translate("root", "Назад"))
        self.groupBox_4.setTitle(_translate("root", "Центр фигуры"))
        self.lb_x0.setText(_translate("root", "x0:"))
        self.en_x0.setText(_translate("root", "0"))
        self.lb_y0.setText(_translate("root", "y0:"))
        self.en_y0.setText(_translate("root", "0"))
        self.label.setText(_translate("root", "Величины смещения, а также центры масштабирования и поворота указываются в пикселях. Угол поворота - в градусах. На рисунке проведены оси OX и OY с засечками каждые 100 пикселей. "))
