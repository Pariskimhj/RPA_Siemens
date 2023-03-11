# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SAP_UI.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QPushButton{\n"
"	background-color: rgba(0,0,0,0)\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	color: rgb(255,255,255);\n"
"	background-color: rgb(0,0,0);\n"
"	border-radius: 15px;\n"
"}\n"
"\n"
"QFrame{\n"
"	background-color: rgb(255, 255, 255);\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_home = QPushButton(self.frame)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 33))
        font = QFont()
        font.setPointSize(11)
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btn_home)

        self.btn_sap = QPushButton(self.frame)
        self.btn_sap.setObjectName(u"btn_sap")
        self.btn_sap.setMinimumSize(QSize(0, 33))
        self.btn_sap.setFont(font)
        self.btn_sap.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btn_sap)

        self.btn_about = QPushButton(self.frame)
        self.btn_about.setObjectName(u"btn_about")
        self.btn_about.setMinimumSize(QSize(0, 33))
        self.btn_about.setFont(font)
        self.btn_about.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btn_about)

        self.btn_contacts = QPushButton(self.frame)
        self.btn_contacts.setObjectName(u"btn_contacts")
        self.btn_contacts.setMinimumSize(QSize(0, 33))
        self.btn_contacts.setFont(font)
        self.btn_contacts.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.btn_contacts)


        self.verticalLayout.addWidget(self.frame)

        self.Pages = QStackedWidget(self.centralwidget)
        self.Pages.setObjectName(u"Pages")
        self.Pages.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout_2 = QVBoxLayout(self.pg_home)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.pg_home)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_2.addWidget(self.label_2)

        self.Pages.addWidget(self.pg_home)
        self.pg_sap = QWidget()
        self.pg_sap.setObjectName(u"pg_sap")
        self.verticalLayout_4 = QVBoxLayout(self.pg_sap)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.pg_sap)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_4.addWidget(self.label_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.txt_file = QLineEdit(self.pg_sap)
        self.txt_file.setObjectName(u"txt_file")
        self.txt_file.setFont(font)
        self.txt_file.setCursor(QCursor(Qt.ArrowCursor))
        self.txt_file.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.txt_file)

        self.btn_open = QPushButton(self.pg_sap)
        self.btn_open.setObjectName(u"btn_open")
        self.btn_open.setMinimumSize(QSize(100, 30))
        self.btn_open.setStyleSheet(u"QPushButton{\n"
"	color:black;background-color: rgb(247, 247, 247);\n"
"	border-top-right-radius:15px\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(159, 238, 238);\n"
"	color: rgb(47, 47, 47)\n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_open)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.tb_customers = QTableWidget(self.pg_sap)
        if (self.tb_customers.columnCount() < 9):
            self.tb_customers.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.tb_customers.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tb_customers.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tb_customers.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tb_customers.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tb_customers.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tb_customers.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tb_customers.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tb_customers.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tb_customers.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tb_customers.setObjectName(u"tb_customers")

        self.horizontalLayout_3.addWidget(self.tb_customers)

        self.frame_2 = QFrame(self.pg_sap)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QPushButton{\n"
"\n"
"	color:black;\n"
"	background-color: rgb(248,248,248);\n"
"	border-radius: 15px;\n"
"\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"	background-color:rgb(159, 238, 238);\n"
"color: rgb(47, 47, 47)\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_login = QPushButton(self.frame_2)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setMinimumSize(QSize(100, 30))
        font1 = QFont()
        font1.setPointSize(10)
        self.btn_login.setFont(font1)
        self.btn_login.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.btn_login)

        self.btn_AssetList = QPushButton(self.frame_2)
        self.btn_AssetList.setObjectName(u"btn_AssetList")
        self.btn_AssetList.setMinimumSize(QSize(0, 30))
        self.btn_AssetList.setFont(font1)
        self.btn_AssetList.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.btn_AssetList)

        self.btn_search = QPushButton(self.frame_2)
        self.btn_search.setObjectName(u"btn_search")
        self.btn_search.setMinimumSize(QSize(0, 30))
        self.btn_search.setFont(font1)
        self.btn_search.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.btn_search)

        self.btn_change = QPushButton(self.frame_2)
        self.btn_change.setObjectName(u"btn_change")
        self.btn_change.setMinimumSize(QSize(0, 30))
        self.btn_change.setFont(font1)
        self.btn_change.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.btn_change)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.btn_close = QPushButton(self.frame_2)
        self.btn_close.setObjectName(u"btn_close")
        self.btn_close.setMinimumSize(QSize(0, 30))
        self.btn_close.setFont(font1)
        self.btn_close.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.btn_close)


        self.horizontalLayout_3.addWidget(self.frame_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.Pages.addWidget(self.pg_sap)
        self.pg_about = QWidget()
        self.pg_about.setObjectName(u"pg_about")
        self.verticalLayout_6 = QVBoxLayout(self.pg_about)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_4 = QLabel(self.pg_about)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_6.addWidget(self.label_4)

        self.label_6 = QLabel(self.pg_about)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setWordWrap(True)

        self.verticalLayout_6.addWidget(self.label_6)

        self.Pages.addWidget(self.pg_about)
        self.pg_contacts = QWidget()
        self.pg_contacts.setObjectName(u"pg_contacts")
        self.verticalLayout_5 = QVBoxLayout(self.pg_contacts)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_5 = QLabel(self.pg_contacts)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_5.addWidget(self.label_5)

        self.label = QLabel(self.pg_contacts)
        self.label.setObjectName(u"label")

        self.verticalLayout_5.addWidget(self.label)

        self.Pages.addWidget(self.pg_contacts)

        self.verticalLayout.addWidget(self.Pages)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.Pages.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_sap.setText(QCoreApplication.translate("MainWindow", u"SAP", None))
        self.btn_about.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.btn_contacts.setText(QCoreApplication.translate("MainWindow", u"Contacts", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600;\">HeeJi</span></p><p align=\"center\"><span style=\" font-size:16pt;\">AUTOMATION SAP SYSTEM</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">SAP - Customers</span></p></body></html>", None))
        self.txt_file.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Select Excel file", None))
        self.btn_open.setText(QCoreApplication.translate("MainWindow", u"Open File", None))
        ___qtablewidgetitem = self.tb_customers.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem1 = self.tb_customers.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Customer", None));
        ___qtablewidgetitem2 = self.tb_customers.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem3 = self.tb_customers.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Street", None));
        ___qtablewidgetitem4 = self.tb_customers.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"House Number", None));
        ___qtablewidgetitem5 = self.tb_customers.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Postal Code", None));
        ___qtablewidgetitem6 = self.tb_customers.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"City", None));
        ___qtablewidgetitem7 = self.tb_customers.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Region", None));
        ___qtablewidgetitem8 = self.tb_customers.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Search Term", None));
        self.btn_login.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.btn_AssetList.setText(QCoreApplication.translate("MainWindow", u"AssetList", None))
        self.btn_search.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.btn_change.setText(QCoreApplication.translate("MainWindow", u"Change", None))
        self.btn_close.setText(QCoreApplication.translate("MainWindow", u"Close SAP", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">About</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">This project was developed with the objective of teaching how to automate process in SAP for free.</span></p><p align=\"center\"><span style=\" font-size:14pt;\">here, you will learn how to create a graphical interface using Qt Designer and how to use Pyside2.</span></p><p align=\"center\"><span style=\" font-size:14pt;\">You will also learn to use tables that will be very useful in your projects.</span></p></body></html>", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Contacts</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">EMAIL : heeji.kim.ext@siemens-healthineers.com</span></p></body></html>", None))
    # retranslateUi

