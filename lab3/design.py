# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(2400, 1300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.box_alg = QtWidgets.QComboBox(self.centralwidget)
        self.box_alg.setGeometry(QtCore.QRect(20, 80, 391, 71))
        self.box_alg.setObjectName("box_alg")
        self.box_alg.addItem("")
        self.box_alg.addItem("")
        self.box_alg.addItem("")
        self.box_alg.addItem("")
        self.box_alg.addItem("")
        self.box_alg.addItem("")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 421, 51))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 170, 421, 51))
        self.label_2.setObjectName("label_2")
        self.box_color = QtWidgets.QComboBox(self.centralwidget)
        self.box_color.setGeometry(QtCore.QRect(20, 220, 391, 71))
        self.box_color.setObjectName("box_color")
        self.box_color.addItem("")
        self.box_color.addItem("")
        self.box_color.addItem("")
        self.box_color.addItem("")
        self.box_color.addItem("")
        self.box_color.addItem("")
        self.box_color.addItem("")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(19, 339, 481, 261))
        self.groupBox.setObjectName("groupBox")
        self.box_xn = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.box_xn.setGeometry(QtCore.QRect(60, 70, 131, 41))
        self.box_xn.setMinimum(-10000.0)
        self.box_xn.setMaximum(10000.0)
        self.box_xn.setSingleStep(100.0)
        self.box_xn.setObjectName("box_xn")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 47, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 130, 47, 41))
        self.label_4.setObjectName("label_4")
        self.box_yn = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.box_yn.setGeometry(QtCore.QRect(60, 130, 131, 41))
        self.box_yn.setMinimum(-10000.0)
        self.box_yn.setMaximum(10000.0)
        self.box_yn.setSingleStep(100.0)
        self.box_yn.setObjectName("box_yn")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(230, 70, 47, 41))
        self.label_5.setObjectName("label_5")
        self.box_yk = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.box_yk.setGeometry(QtCore.QRect(280, 130, 131, 41))
        self.box_yk.setMinimum(-10000.0)
        self.box_yk.setMaximum(10000.0)
        self.box_yk.setSingleStep(100.0)
        self.box_yk.setProperty("value", 100.0)
        self.box_yk.setObjectName("box_yk")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(230, 130, 47, 41))
        self.label_6.setObjectName("label_6")
        self.box_xk = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.box_xk.setGeometry(QtCore.QRect(280, 70, 131, 41))
        self.box_xk.setMinimum(-10000.0)
        self.box_xk.setMaximum(10000.0)
        self.box_xk.setSingleStep(100.0)
        self.box_xk.setProperty("value", 100.0)
        self.box_xk.setObjectName("box_xk")
        self.but_single = QtWidgets.QPushButton(self.groupBox)
        self.but_single.setGeometry(QtCore.QRect(30, 200, 421, 51))
        self.but_single.setObjectName("but_single")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 620, 481, 261))
        self.groupBox_2.setObjectName("groupBox_2")
        self.box_xc = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.box_xc.setGeometry(QtCore.QRect(60, 70, 131, 41))
        self.box_xc.setMinimum(-10000.0)
        self.box_xc.setMaximum(10000.0)
        self.box_xc.setSingleStep(100.0)
        self.box_xc.setObjectName("box_xc")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(10, 70, 47, 41))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(10, 130, 47, 41))
        self.label_8.setObjectName("label_8")
        self.box_yc = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.box_yc.setGeometry(QtCore.QRect(60, 130, 131, 41))
        self.box_yc.setMinimum(-10000.0)
        self.box_yc.setMaximum(10000.0)
        self.box_yc.setSingleStep(100.0)
        self.box_yc.setObjectName("box_yc")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(230, 70, 101, 41))
        self.label_9.setObjectName("label_9")
        self.box_step = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.box_step.setGeometry(QtCore.QRect(340, 130, 131, 41))
        self.box_step.setMinimum(0.1)
        self.box_step.setMaximum(10000.0)
        self.box_step.setSingleStep(10.0)
        self.box_step.setProperty("value", 30.0)
        self.box_step.setObjectName("box_step")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(230, 130, 101, 41))
        self.label_10.setObjectName("label_10")
        self.box_len = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.box_len.setGeometry(QtCore.QRect(340, 70, 131, 41))
        self.box_len.setMinimum(0.0)
        self.box_len.setMaximum(10000.0)
        self.box_len.setSingleStep(100.0)
        self.box_len.setProperty("value", 200.0)
        self.box_len.setObjectName("box_len")
        self.but_bunch = QtWidgets.QPushButton(self.groupBox_2)
        self.but_bunch.setGeometry(QtCore.QRect(30, 200, 421, 51))
        self.but_bunch.setObjectName("but_bunch")
        self.but_time = QtWidgets.QPushButton(self.centralwidget)
        self.but_time.setGeometry(QtCore.QRect(20, 950, 491, 51))
        self.but_time.setObjectName("but_time")
        self.but_step = QtWidgets.QPushButton(self.centralwidget)
        self.but_step.setGeometry(QtCore.QRect(20, 1020, 491, 51))
        self.but_step.setObjectName("but_step")
        self.but_axes = QtWidgets.QPushButton(self.centralwidget)
        self.but_axes.setGeometry(QtCore.QRect(20, 1130, 491, 51))
        self.but_axes.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.but_axes.setAutoRepeat(False)
        self.but_axes.setObjectName("but_axes")
        self.but_clean = QtWidgets.QPushButton(self.centralwidget)
        self.but_clean.setGeometry(QtCore.QRect(20, 1200, 491, 51))
        self.but_clean.setObjectName("but_clean")
        self.graph = QtWidgets.QGraphicsView(self.centralwidget)
        self.graph.setGeometry(QtCore.QRect(614, 29, 1700, 1200))
        self.graph.setObjectName("graph")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(486, 30, 121, 51))
        self.label_11.setObjectName("label_11")
        self.box_width = QtWidgets.QSpinBox(self.centralwidget)
        self.box_width.setGeometry(QtCore.QRect(491, 81, 111, 71))
        self.box_width.setMinimum(1)
        self.box_width.setMaximum(10)
        self.box_width.setObjectName("box_width")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Алгоритмы построения отрезков"))
        self.box_alg.setItemText(0, _translate("MainWindow", "ЦДА"))
        self.box_alg.setItemText(1, _translate("MainWindow", "Брезенхем (действ.)"))
        self.box_alg.setItemText(2, _translate("MainWindow", "Брезенхем (цел.)"))
        self.box_alg.setItemText(3, _translate("MainWindow", "Брезенхем (устр. ступенч.)"))
        self.box_alg.setItemText(4, _translate("MainWindow", "Ву"))
        self.box_alg.setItemText(5, _translate("MainWindow", "Библиотечная функция"))
        self.label.setText(_translate("MainWindow", "Выберите алгоритм построения:"))
        self.label_2.setText(_translate("MainWindow", "Выберите цвет:"))
        self.box_color.setItemText(0, _translate("MainWindow", "Черный"))
        self.box_color.setItemText(1, _translate("MainWindow", "Красный"))
        self.box_color.setItemText(2, _translate("MainWindow", "Зеленый"))
        self.box_color.setItemText(3, _translate("MainWindow", "Синий"))
        self.box_color.setItemText(4, _translate("MainWindow", "Желтый"))
        self.box_color.setItemText(5, _translate("MainWindow", "Розовый"))
        self.box_color.setItemText(6, _translate("MainWindow", "Цвет фона"))
        self.groupBox.setTitle(_translate("MainWindow", "Построение одиночного отрезка"))
        self.label_3.setText(_translate("MainWindow", "Xn:"))
        self.label_4.setText(_translate("MainWindow", "Yn:"))
        self.label_5.setText(_translate("MainWindow", "Xk:"))
        self.label_6.setText(_translate("MainWindow", "Yk:"))
        self.but_single.setText(_translate("MainWindow", "Построить орезок"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Построение пучка отрезков"))
        self.label_7.setText(_translate("MainWindow", "Xс:"))
        self.label_8.setText(_translate("MainWindow", "Yс:"))
        self.label_9.setText(_translate("MainWindow", "Длина:"))
        self.label_10.setText(_translate("MainWindow", "Шаг, °:"))
        self.but_bunch.setText(_translate("MainWindow", "Построить пучок"))
        self.but_time.setText(_translate("MainWindow", "Сравнить временные характеристики"))
        self.but_step.setText(_translate("MainWindow", "Исследовать ступенчатость"))
        self.but_axes.setText(_translate("MainWindow", "Показать/скрыть оси"))
        self.but_clean.setText(_translate("MainWindow", "Очистить экран"))
        self.label_11.setText(_translate("MainWindow", "Толщина:"))
