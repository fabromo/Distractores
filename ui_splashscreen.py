# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splashscreenHfQvBE.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_SplashScreen(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"	color:#FFF;\n"
"}\n"
"QWidget{\n"
"	background: rgb(0, 61, 90)\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.applogo = QFrame(self.centralwidget)
        self.applogo.setObjectName(u"applogo")
        self.applogo.setMinimumSize(QSize(0, 200))
        self.applogo.setFrameShape(QFrame.StyledPanel)
        self.applogo.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.applogo)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.logoimg = QLabel(self.applogo)
        self.logoimg.setObjectName(u"logoimg")
        self.logoimg.setMinimumSize(QSize(100, 100))
        self.logoimg.setMaximumSize(QSize(100, 100))
        self.logoimg.setSizeIncrement(QSize(100, 100))
        self.logoimg.setStyleSheet(u"QLabel{\n"
"	background: #FFF;\n"
"	border-radius:50px;\n"
"}")
        self.logoimg.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.logoimg)


        self.verticalLayout.addWidget(self.applogo)

        self.background = QFrame(self.centralwidget)
        self.background.setObjectName(u"background")
        self.background.setFrameShape(QFrame.StyledPanel)
        self.background.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.background)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.app_name = QLabel(self.background)
        self.app_name.setObjectName(u"app_name")
        font = QFont()
        font.setFamily(u"Roboto")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        self.app_name.setFont(font)
        self.app_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.app_name)

        self.app_description = QLabel(self.background)
        self.app_description.setObjectName(u"app_description")
        font1 = QFont()
        font1.setFamily(u"Roboto")
        font1.setPointSize(18)
        self.app_description.setFont(font1)
        self.app_description.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.app_description)

        self.footer = QFrame(self.background)
        self.footer.setObjectName(u"footer")
        self.footer.setFrameShape(QFrame.StyledPanel)
        self.footer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.footer)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.status = QLabel(self.footer)
        self.status.setObjectName(u"status")
        font2 = QFont()
        font2.setFamily(u"Poppins")
        font2.setPointSize(14)
        font2.setBold(False)
        font2.setWeight(50)
        self.status.setFont(font2)

        self.horizontalLayout_2.addWidget(self.status)

        self.author = QLabel(self.footer)
        self.author.setObjectName(u"author")
        self.author.setFont(font2)
        self.author.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.author)


        self.verticalLayout_2.addWidget(self.footer)

        self.progress = QFrame(self.background)
        self.progress.setObjectName(u"progress")
        font3 = QFont()
        font3.setFamily(u"Poppins")
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setWeight(75)
        self.progress.setFont(font3)
        self.progress.setFrameShape(QFrame.StyledPanel)
        self.progress.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.progress)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(30, -1, 30, -1)
        self.percentage = QLabel(self.progress)
        self.percentage.setObjectName(u"percentage")
        self.percentage.setFont(font2)
        self.percentage.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.percentage)

        self.progressBar = QProgressBar(self.progress)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(0, 10))
        self.progressBar.setMaximumSize(QSize(16777215, 10))
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"	background:rgba(255, 255, 255, 180);\n"
"	border-style: none;\n"
"	border-radius: 5px;\n"
"	color:rgba(200, 200, 200, 0)\n"
"	text-align:center; \n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"	border-radius:5px;\n"
"background-color:qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(254, 170, 199, 255), stop:1 rgba(100, 85, 255, 255))\n"
"	\n"
"}")
        self.progressBar.setValue(24)

        self.verticalLayout_3.addWidget(self.progressBar)


        self.verticalLayout_2.addWidget(self.progress)


        self.verticalLayout.addWidget(self.background)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Mensaje de alerta!", None))
        self.logoimg.setText(QCoreApplication.translate("MainWindow", u"logo", None))
        self.app_name.setText(QCoreApplication.translate("MainWindow", u"App Name", None))
        self.app_description.setText(QCoreApplication.translate("MainWindow", u"App Description", None))
        self.status.setText(QCoreApplication.translate("MainWindow", u"status", None))
        self.author.setText(QCoreApplication.translate("MainWindow", u"Author: Fabricio Morales", None))
        self.percentage.setText(QCoreApplication.translate("MainWindow", u"Percentage", None))
    # retranslateUi

