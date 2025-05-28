# -*- coding: utf-8 -*-
from PyQt5.QtCore import QRect, QMetaObject, QCoreApplication
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QWidget, QLineEdit, QPushButton
################################################################################
## Form generated from reading UI file 'calculadora-2ElrrdO.ui'
##
## Created by: Qt User Interface Compiler version 5.15.13
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *  # type: ignore
from PySide2.QtGui import *  # type: ignore
from PySide2.QtWidgets import *  # type: ignore

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(326, 328)
        MainWindow.setStyleSheet(u"background-color:rgb(94, 92, 100);\n"
"border-color: rgb(61, 56, 70);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.display = QLineEdit(self.centralwidget)
        self.display.setObjectName(u"display")
        self.display.setGeometry(QRect(10, 20, 301, 41))
        self.display.setStyleSheet(u"background-color:  rgb(222, 221, 218);\n"
"border-color: rgb(94, 92, 100);\n"
"border-radius: 0px")
        self.btSete = QPushButton(self.centralwidget)
        self.btSete.setObjectName(u"btSete")
        self.btSete.setGeometry(QRect(20, 80, 51, 51))
        font = QFont()
        font.setPointSize(24)
        self.btSete.setFont(font)
        self.btSete.setStyleSheet(u"background-color: rgb(222, 221, 218);\n"
"border-radius: 0px")
        self.btOito = QPushButton(self.centralwidget)
        self.btOito.setObjectName(u"btOito")
        self.btOito.setGeometry(QRect(80, 80, 51, 51))
        self.btOito.setFont(font)
        self.btOito.setStyleSheet(u"background-color: rgb(222, 221, 218);\n"
"border-radius: 0px")
        self.btNove = QPushButton(self.centralwidget)
        self.btNove.setObjectName(u"btNove")
        self.btNove.setGeometry(QRect(140, 80, 51, 51))
        self.btNove.setFont(font)
        self.btNove.setStyleSheet(u"background-color: rgb(222, 221, 218);\n"
"border-radius: 0px")
        self.btQuatro = QPushButton(self.centralwidget)
        self.btQuatro.setObjectName(u"btQuatro")
        self.btQuatro.setGeometry(QRect(20, 140, 51, 51))
        self.btQuatro.setFont(font)
        self.btQuatro.setStyleSheet(u"background-color: rgb(222, 221, 218);\n"
"border-radius: 0px")
        self.btCinco = QPushButton(self.centralwidget)
        self.btCinco.setObjectName(u"btCinco")
        self.btCinco.setGeometry(QRect(80, 140, 51, 51))
        self.btCinco.setFont(font)
        self.btCinco.setStyleSheet(u"background-color: rgb(222, 221, 218);\n"
"border-radius: 0px")
        self.btSeis = QPushButton(self.centralwidget)
        self.btSeis.setObjectName(u"btSeis")
        self.btSeis.setGeometry(QRect(140, 140, 51, 51))
        self.btSeis.setFont(font)
        self.btSeis.setStyleSheet(u"background-color: rgb(222, 221, 218);\n"
"border-radius: 0px")
        self.btUm = QPushButton(self.centralwidget)
        self.btUm.setObjectName(u"btUm")
        self.btUm.setGeometry(QRect(20, 200, 51, 51))
        self.btUm.setFont(font)
        self.btUm.setStyleSheet(u"background-color: rgb(222, 221, 218);\n"
"border-radius: 0px")
        self.btDois = QPushButton(self.centralwidget)
        self.btDois.setObjectName(u"btDois")
        self.btDois.setGeometry(QRect(80, 200, 51, 51))
        self.btDois.setFont(font)
        self.btDois.setStyleSheet(u"background-color: rgb(222, 221, 218);\n"
"border-radius: 0px")
        self.btTres = QPushButton(self.centralwidget)
        self.btTres.setObjectName(u"btTres")
        self.btTres.setGeometry(QRect(140, 200, 51, 51))
        self.btTres.setFont(font)
        self.btTres.setStyleSheet(u"background-color: rgb(222, 221, 218);\n"
"border-radius: 0px")
        self.btZero = QPushButton(self.centralwidget)
        self.btZero.setObjectName(u"btZero")
        self.btZero.setGeometry(QRect(20, 260, 110, 50))
        self.btZero.setFont(font)
        self.btZero.setStyleSheet(u"background-color: rgb(222, 221, 218);\n"
"border-radius: 0px")
        self.btPonto = QPushButton(self.centralwidget)
        self.btPonto.setObjectName(u"btPonto")
        self.btPonto.setGeometry(QRect(140, 260, 50, 50))
        self.btPonto.setFont(font)
        self.btPonto.setStyleSheet(u"background-color: rgb(255, 190, 111);\n"
"border-radius: 0px")
        self.btIgual = QPushButton(self.centralwidget)
        self.btIgual.setObjectName(u"btIgual")
        self.btIgual.setGeometry(QRect(260, 79, 50, 231))
        self.btIgual.setFont(font)
        self.btIgual.setStyleSheet(u"background-color: orange;\n"
"border-radius: 0px")
        self.btMais = QPushButton(self.centralwidget)
        self.btMais.setObjectName(u"btMais")
        self.btMais.setGeometry(QRect(200, 80, 50, 51))
        self.btMais.setFont(font)
        self.btMais.setStyleSheet(u"background-color: rgb(255, 190, 111);\n"
"border-radius: 0px")
        self.btMenos = QPushButton(self.centralwidget)
        self.btMenos.setObjectName(u"btMenos")
        self.btMenos.setGeometry(QRect(200, 260, 51, 51))
        font1 = QFont()
        font1.setPointSize(22)
        self.btMenos.setFont(font1)
        self.btMenos.setStyleSheet(u"background-color: rgb(255, 190, 111);\n"
"border-radius: 0px")
        self.btDiv = QPushButton(self.centralwidget)
        self.btDiv.setObjectName(u"btDiv")
        self.btDiv.setGeometry(QRect(200, 140, 51, 51))
        self.btDiv.setFont(font)
        self.btDiv.setStyleSheet(u"background-color: rgb(255, 190, 111);\n"
"border-radius: 0px")
        self.btMult = QPushButton(self.centralwidget)
        self.btMult.setObjectName(u"btMult")
        self.btMult.setGeometry(QRect(200, 200, 51, 51))
        self.btMult.setFont(font)
        self.btMult.setStyleSheet(u"background-color: rgb(255, 190, 111);\n"
"border-radius: 0px")
        MainWindow.setCentralWidget(self.centralwidget)
        self.btSete.raise_()
        self.btOito.raise_()
        self.btNove.raise_()
        self.btQuatro.raise_()
        self.btCinco.raise_()
        self.btSeis.raise_()
        self.btUm.raise_()
        self.btDois.raise_()
        self.btTres.raise_()
        self.btZero.raise_()
        self.btPonto.raise_()
        self.btIgual.raise_()
        self.btMais.raise_()
        self.btMenos.raise_()
        self.btDiv.raise_()
        self.btMult.raise_()
        self.display.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Calculadora ultra 3000", None))
        self.btSete.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.btOito.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.btNove.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.btQuatro.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.btCinco.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.btSeis.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.btUm.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.btDois.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.btTres.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.btZero.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btPonto.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.btIgual.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.btMais.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.btMenos.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.btDiv.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.btMult.setText(QCoreApplication.translate("MainWindow", u"x", None))
    # retranslateUi



