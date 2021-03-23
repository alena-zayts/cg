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
        self.groupBox.setGeometry(QtCore.QRect(20, 330, 591, 411))
        self.groupBox.setObjectName("groupBox")
        self.box_c_xc = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.box_c_xc.setGeometry(QtCore.QRect(100, 160, 131, 41))
        self.box_c_xc.setMinimum(-10000.0)
        self.box_c_xc.setMaximum(10000.0)
        self.box_c_xc.setSingleStep(100.0)
        self.box_c_xc.setObjectName("box_c_xc")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 160, 47, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 220, 47, 41))
        self.label_4.setObjectName("label_4")
        self.box_c_yc = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.box_c_yc.setGeometry(QtCore.QRect(100, 220, 131, 41))
        self.box_c_yc.setMinimum(-10000.0)
        self.box_c_yc.setMaximum(10000.0)
        self.box_c_yc.setSingleStep(100.0)
        self.box_c_yc.setObjectName("box_c_yc")
        self.box_c_step = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.box_c_step.setGeometry(QtCore.QRect(360, 220, 131, 41))
        self.box_c_step.setMinimum(1.0)
        self.box_c_step.setMaximum(10000.0)
        self.box_c_step.setSingleStep(10.0)
        self.box_c_step.setProperty("value", 50.0)
        self.box_c_step.setObjectName("box_c_step")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(290, 220, 71, 41))
        self.label_6.setObjectName("label_6")
        self.but_circle = QtWidgets.QPushButton(self.groupBox)
        self.but_circle.setGeometry(QtCore.QRect(30, 340, 191, 51))
        self.but_circle.setObjectName("but_circle")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 280, 91, 41))
        self.label_5.setObjectName("label_5")
        self.box_c_r1 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.box_c_r1.setGeometry(QtCore.QRect(100, 280, 131, 41))
        self.box_c_r1.setMinimum(0.0)
        self.box_c_r1.setMaximum(10000.0)
        self.box_c_r1.setSingleStep(100.0)
        self.box_c_r1.setProperty("value", 100.0)
        self.box_c_r1.setObjectName("box_c_r1")
        self.box_c_param = QtWidgets.QComboBox(self.groupBox)
        self.box_c_param.setGeometry(QtCore.QRect(230, 90, 301, 41))
        self.box_c_param.setObjectName("box_c_param")
        self.box_c_param.addItem("")
        self.box_c_param.addItem("")
        self.box_c_param.addItem("")
        self.box_c_param.addItem("")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(230, 50, 291, 41))
        self.label_12.setObjectName("label_12")
        self.box_c_r2 = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.box_c_r2.setGeometry(QtCore.QRect(360, 160, 131, 41))
        self.box_c_r2.setMinimum(0.0)
        self.box_c_r2.setMaximum(10000.0)
        self.box_c_r2.setSingleStep(100.0)
        self.box_c_r2.setProperty("value", 500.0)
        self.box_c_r2.setObjectName("box_c_r2")
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(290, 160, 71, 41))
        self.label_13.setObjectName("label_13")
        self.box_c_n = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.box_c_n.setGeometry(QtCore.QRect(360, 280, 131, 41))
        self.box_c_n.setDecimals(0)
        self.box_c_n.setMinimum(1.0)
        self.box_c_n.setMaximum(10000.0)
        self.box_c_n.setSingleStep(10.0)
        self.box_c_n.setProperty("value", 10.0)
        self.box_c_n.setObjectName("box_c_n")
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setGeometry(QtCore.QRect(290, 280, 71, 41))
        self.label_14.setObjectName("label_14")
        self.but_circles = QtWidgets.QPushButton(self.groupBox)
        self.but_circles.setGeometry(QtCore.QRect(340, 340, 191, 51))
        self.but_circles.setObjectName("but_circles")
        self.but_time = QtWidgets.QPushButton(self.centralwidget)
        self.but_time.setGeometry(QtCore.QRect(640, 1200, 491, 51))
        self.but_time.setObjectName("but_time")
        self.but_axes = QtWidgets.QPushButton(self.centralwidget)
        self.but_axes.setGeometry(QtCore.QRect(1160, 1200, 491, 51))
        self.but_axes.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.but_axes.setAutoRepeat(False)
        self.but_axes.setObjectName("but_axes")
        self.but_clean = QtWidgets.QPushButton(self.centralwidget)
        self.but_clean.setGeometry(QtCore.QRect(1670, 1200, 491, 51))
        self.but_clean.setObjectName("but_clean")
        self.graph = QtWidgets.QGraphicsView(self.centralwidget)
        self.graph.setGeometry(QtCore.QRect(614, 29, 1700, 1100))
        self.graph.setObjectName("graph")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(486, 30, 121, 51))
        self.label_11.setObjectName("label_11")
        self.box_width = QtWidgets.QSpinBox(self.centralwidget)
        self.box_width.setGeometry(QtCore.QRect(491, 81, 111, 71))
        self.box_width.setMinimum(1)
        self.box_width.setMaximum(10)
        self.box_width.setObjectName("box_width")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 770, 591, 401))
        self.groupBox_2.setObjectName("groupBox_2")
        self.box_e_xc = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.box_e_xc.setGeometry(QtCore.QRect(70, 40, 131, 41))
        self.box_e_xc.setMinimum(-10000.0)
        self.box_e_xc.setMaximum(10000.0)
        self.box_e_xc.setSingleStep(100.0)
        self.box_e_xc.setObjectName("box_e_xc")
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(10, 40, 47, 41))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(10, 100, 47, 41))
        self.label_8.setObjectName("label_8")
        self.box_e_yc = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.box_e_yc.setGeometry(QtCore.QRect(70, 100, 131, 41))
        self.box_e_yc.setMinimum(-10000.0)
        self.box_e_yc.setMaximum(10000.0)
        self.box_e_yc.setSingleStep(100.0)
        self.box_e_yc.setObjectName("box_e_yc")
        self.but_ellipse = QtWidgets.QPushButton(self.groupBox_2)
        self.but_ellipse.setGeometry(QtCore.QRect(30, 320, 191, 51))
        self.but_ellipse.setObjectName("but_ellipse")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(10, 160, 91, 41))
        self.label_10.setObjectName("label_10")
        self.box_e_a = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.box_e_a.setGeometry(QtCore.QRect(70, 160, 131, 41))
        self.box_e_a.setMinimum(0.0)
        self.box_e_a.setMaximum(10000.0)
        self.box_e_a.setSingleStep(100.0)
        self.box_e_a.setProperty("value", 200.0)
        self.box_e_a.setObjectName("box_e_a")
        self.but_ellipses = QtWidgets.QPushButton(self.groupBox_2)
        self.but_ellipses.setGeometry(QtCore.QRect(340, 320, 191, 51))
        self.but_ellipses.setObjectName("but_ellipses")
        self.label_17 = QtWidgets.QLabel(self.groupBox_2)
        self.label_17.setGeometry(QtCore.QRect(10, 220, 71, 41))
        self.label_17.setObjectName("label_17")
        self.box_e_b = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.box_e_b.setGeometry(QtCore.QRect(70, 220, 131, 41))
        self.box_e_b.setMinimum(0.0)
        self.box_e_b.setMaximum(10000.0)
        self.box_e_b.setSingleStep(100.0)
        self.box_e_b.setProperty("value", 100.0)
        self.box_e_b.setObjectName("box_e_b")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Алгоритмы построения отрезков"))
        self.box_alg.setItemText(0, _translate("MainWindow", "Каноническое уравнение"))
        self.box_alg.setItemText(1, _translate("MainWindow", "Параметрическое уравнение"))
        self.box_alg.setItemText(2, _translate("MainWindow", "Алгоритм Брезенхема"))
        self.box_alg.setItemText(3, _translate("MainWindow", "Алгоритм средней точки"))
        self.box_alg.setItemText(4, _translate("MainWindow", "Библиотечная функция"))
        self.label.setText(_translate("MainWindow", "Выберите алгоритм:"))
        self.label_2.setText(_translate("MainWindow", "Выберите цвет:"))
        self.box_color.setItemText(0, _translate("MainWindow", "Черный"))
        self.box_color.setItemText(1, _translate("MainWindow", "Красный"))
        self.box_color.setItemText(2, _translate("MainWindow", "Зеленый"))
        self.box_color.setItemText(3, _translate("MainWindow", "Синий"))
        self.box_color.setItemText(4, _translate("MainWindow", "Желтый"))
        self.box_color.setItemText(5, _translate("MainWindow", "Розовый"))
        self.box_color.setItemText(6, _translate("MainWindow", "Цвет фона"))
        self.groupBox.setTitle(_translate("MainWindow", "Построение окружности (окружностей)"))
        self.label_3.setText(_translate("MainWindow", "Xс:"))
        self.label_4.setText(_translate("MainWindow", "Yс:"))
        self.label_6.setText(_translate("MainWindow", "Step:"))
        self.but_circle.setText(_translate("MainWindow", "Окружность"))
        self.label_5.setText(_translate("MainWindow", "R(beg):"))
        self.box_c_param.setItemText(0, _translate("MainWindow", "Rbeg, Rend, Step"))
        self.box_c_param.setItemText(1, _translate("MainWindow", "Rbeg, Rend, N"))
        self.box_c_param.setItemText(2, _translate("MainWindow", "Rbeg, Step, N"))
        self.box_c_param.setItemText(3, _translate("MainWindow", "Rend, Step, N"))
        self.label_12.setText(_translate("MainWindow", "Параметры спектра"))
        self.label_13.setText(_translate("MainWindow", "Rend:"))
        self.label_14.setText(_translate("MainWindow", "N:"))
        self.but_circles.setText(_translate("MainWindow", "Спектр"))
        self.but_time.setText(_translate("MainWindow", "Сравнить временные характеристики"))
        self.but_axes.setText(_translate("MainWindow", "Показать/скрыть оси"))
        self.but_clean.setText(_translate("MainWindow", "Очистить экран"))
        self.label_11.setText(_translate("MainWindow", "Толщина:"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Построение эллипса (эллипсов)"))
        self.label_7.setText(_translate("MainWindow", "Xс:"))
        self.label_8.setText(_translate("MainWindow", "Yс:"))
        self.but_ellipse.setText(_translate("MainWindow", "Эллипс"))
        self.label_10.setText(_translate("MainWindow", "a:"))
        self.but_ellipses.setText(_translate("MainWindow", "Спектр"))
        self.label_17.setText(_translate("MainWindow", "b:"))
