# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\usuario\OneDrive\Documentos\semestre 2021-3\ciencias 2.2\Colisiones\ventanaColi.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from qt_for_python.rcc.source import * 

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(732, 555)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("*{\n"
"\n"
"     background-image: url(:/images/imagenes/HD-wallpaper-abstract-colorful-colors-pattern-thumbnail.jpg);\n"
"     font-family:     Comic Sans MS;\n"
"}\n"
"\n"
"QLabel{\n"
"    background: rgb(0, 0, 0) transparent;    \n"
"    color:white;\n"
"    font-weight: 900;\n"
"     font-size:25px;\n"
"}\n"
"\n"
"QPushButton{\n"
"   background:#2d89ef;\n"
"   color: white;\n"
"   border: 2px solid;\n"
"   border-radius:15px;\n"
"   font-size:15px;        \n"
"}\n"
"\n"
"QLineEdit{\n"
"  background:white;\n"
"  color:black;    \n"
"  border: 2px solid;\n"
"  border-radius:15px;    \n"
"  font-size:13px;\n"
"}\n"
"\n"
"QWidget#contenedor{\n"
"    background: rgb(0, 0, 0) transparent;\n"
"    border:transparent;\n"
"}\n"
"\n"
"QTableView {\n"
"    color: white;\n"
"    font-size:14px;\n"
"    background: rgb(59, 89, 213);\n"
"}\n"
"\n"
"\n"
"QHeaderView{\n"
"  qproperty-defaultAlignment: AlignHCenter;\n"
"  background: rgb(59, 89, 213);\n"
"  font-weight: bold;\n"
"}\n"
"\n"
"\n"
"")
        MainWindow.setAnimated(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.boton_dispersar = QtWidgets.QPushButton(self.centralwidget)
        self.boton_dispersar.setGeometry(QtCore.QRect(370, 70, 91, 31))
        self.boton_dispersar.setObjectName("boton_dispersar")
        self.text_ingresar = QtWidgets.QLineEdit(self.centralwidget)
        self.text_ingresar.setGeometry(QtCore.QRect(40, 50, 311, 31))
        self.text_ingresar.setObjectName("text_ingresar")
        self.contenedor = QtWidgets.QWidget(self.centralwidget)
        self.contenedor.setGeometry(QtCore.QRect(30, 200, 681, 351))
        self.contenedor.setObjectName("contenedor")
        self.tabWidget = QtWidgets.QTabWidget(self.contenedor)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 671, 331))
        self.tabWidget.setObjectName("tabWidget")
        self.EncaLineal = QtWidgets.QWidget()
        self.EncaLineal.setObjectName("EncaLineal")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.EncaLineal)
        self.tabWidget_2.setGeometry(QtCore.QRect(0, 0, 671, 311))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tablaEncaCabe = QtWidgets.QTableWidget(self.tab_4)
        self.tablaEncaCabe.setGeometry(QtCore.QRect(150, 10, 331, 261))
        self.tablaEncaCabe.setObjectName("tablaEncaCabe")
        self.tablaEncaCabe.setColumnCount(0)
        self.tablaEncaCabe.setRowCount(0)
        self.tablaEncaCabe.verticalHeader().setVisible(False)
        self.tabWidget_2.addTab(self.tab_4, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.tablaEncaLisPos = QtWidgets.QTableWidget(self.tab_5)
        self.tablaEncaLisPos.setGeometry(QtCore.QRect(10, 140, 641, 86))
        self.tablaEncaLisPos.setObjectName("tablaEncaLisPos")
        self.tablaEncaLisPos.setColumnCount(0)
        self.tablaEncaLisPos.setRowCount(0)
        self.tablaEncaLisPos.verticalHeader().setVisible(True)
        self.tablaEncaCurs = QtWidgets.QTableWidget(self.tab_5)
        self.tablaEncaCurs.setGeometry(QtCore.QRect(10, 0, 641, 131))
        self.tablaEncaCurs.setObjectName("tablaEncaCurs")
        self.tablaEncaCurs.setColumnCount(0)
        self.tablaEncaCurs.setRowCount(0)
        self.tablaEncaCurs.verticalHeader().setVisible(True)
        self.tabWidget_2.addTab(self.tab_5, "")
        self.tabWidget.addTab(self.EncaLineal, "")
        self.DobleHash = QtWidgets.QWidget()
        self.DobleHash.setObjectName("DobleHash")
        self.tablaDobCurs = QtWidgets.QTableWidget(self.DobleHash)
        self.tablaDobCurs.setGeometry(QtCore.QRect(20, 90, 631, 111))
        self.tablaDobCurs.setObjectName("tablaDobCurs")
        self.tablaDobCurs.setColumnCount(0)
        self.tablaDobCurs.setRowCount(0)
        self.tablaDobCurs.horizontalHeader().setVisible(False)
        self.tablaDobCurs.verticalHeader().setVisible(True)
        self.tabWidget.addTab(self.DobleHash, "")
        self.Cudratica = QtWidgets.QWidget()
        self.Cudratica.setObjectName("Cudratica")
        self.tablaCuaCurs = QtWidgets.QTableWidget(self.Cudratica)
        self.tablaCuaCurs.setGeometry(QtCore.QRect(20, 90, 631, 131))
        self.tablaCuaCurs.setObjectName("tablaCuaCurs")
        self.tablaCuaCurs.setColumnCount(0)
        self.tablaCuaCurs.setRowCount(0)
        self.tablaCuaCurs.verticalHeader().setVisible(True)
        self.tabWidget.addTab(self.Cudratica, "")
        self.boton_eliminar = QtWidgets.QPushButton(self.centralwidget)
        self.boton_eliminar.setGeometry(QtCore.QRect(590, 50, 101, 31))
        self.boton_eliminar.setObjectName("boton_eliminar")
        self.text_ingresar_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.text_ingresar_2.setGeometry(QtCore.QRect(40, 90, 311, 31))
        self.text_ingresar_2.setObjectName("text_ingresar_2")
        self.text_ingresar_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.text_ingresar_3.setGeometry(QtCore.QRect(490, 50, 91, 31))
        self.text_ingresar_3.setObjectName("text_ingresar_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 150, 381, 41))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(99)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.text_ingresarPrimo = QtWidgets.QLineEdit(self.centralwidget)
        self.text_ingresarPrimo.setGeometry(QtCore.QRect(490, 90, 91, 31))
        self.text_ingresarPrimo.setObjectName("text_ingresarPrimo")
        self.boton_AgregarPrimo = QtWidgets.QPushButton(self.centralwidget)
        self.boton_AgregarPrimo.setGeometry(QtCore.QRect(590, 90, 91, 31))
        self.boton_AgregarPrimo.setObjectName("boton_AgregarPrimo")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.boton_dispersar.setText(_translate("MainWindow", "Dispersar"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_4), _translate("MainWindow", "Tab 1"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), _translate("MainWindow", "Tab 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.EncaLineal), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.DobleHash), _translate("MainWindow", "Tab 2"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Cudratica), _translate("MainWindow", "Página"))
        self.boton_eliminar.setText(_translate("MainWindow", "Eliminar"))
        self.label.setText(_translate("MainWindow", "Disponible:"))
        self.boton_AgregarPrimo.setText(_translate("MainWindow", "Primo"))

