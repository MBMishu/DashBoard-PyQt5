# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interface.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1033, 819)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"color:#fff;\n"
"font-size:12px;\n"
"border:none;\n"
"background:none;\n"
"}\n"
"#centralwidget{\n"
"background-color: rgb(33,43,51);\n"
"}\n"
"\n"
"#header_frame, #frame_3, #frame_5{\n"
"background-color: rgb(61, 80, 95,100);\n"
"}\n"
"\n"
"#frame_4 QPushButton{\n"
"background-color: rgb(33, 43, 51,100);\n"
"padding:10px;\n"
"border-radius:5px;\n"
"text-align:left;\n"
"}\n"
"\n"
"#frame_10 QPushButton{\n"
"background-color: rgb(61, 80, 95,100);\n"
"border:3px solid rgb(120,157,186);\n"
"border-radius:15px;\n"
"}\n"
"\n"
"#frame_10 QPushButton:hover{\n"
"background-color: rgb(120,157,186,100);\n"
"}\n"
"\n"
"#left_menu_widget, #percentage_chart,#nested_chart,#line_chart,#bar_chart,#temp_chart{\n"
"background-color: rgb(120,157,186,100);\n"
"}\n"
"\n"
"\n"
"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left_menu_widget = QWidget(self.centralwidget)
        self.left_menu_widget.setObjectName(u"left_menu_widget")
        self.verticalLayout = QVBoxLayout(self.left_menu_widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(7, 7, 0, 7)
        self.frame_3 = QFrame(self.left_menu_widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_3)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.frame_3)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(120, 40))
        self.label_14.setMaximumSize(QSize(120, 40))
        self.label_14.setPixmap(QPixmap(u":/images/logo_white.png"))
        self.label_14.setScaledContents(True)

        self.verticalLayout_12.addWidget(self.label_14)


        self.verticalLayout.addWidget(self.frame_3, 0, Qt.AlignTop)

        self.frame_4 = QFrame(self.left_menu_widget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 12, -1, 0)
        self.pushButton = QPushButton(self.frame_4)
        self.pushButton.setObjectName(u"pushButton")
        icon = QIcon()
        icon.addFile(u":/icons/icons/bar-chart-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.pushButton)

        self.pushButton_5 = QPushButton(self.frame_4)
        self.pushButton_5.setObjectName(u"pushButton_5")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/thermometer.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon1)
        self.pushButton_5.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.pushButton_5)

        self.pushButton_2 = QPushButton(self.frame_4)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/target.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_4 = QPushButton(self.frame_4)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/git-merge.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.pushButton_4)

        self.pushButton_3 = QPushButton(self.frame_4)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/bar-chart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon4)
        self.pushButton_3.setIconSize(QSize(24, 24))

        self.verticalLayout_2.addWidget(self.pushButton_3)


        self.verticalLayout.addWidget(self.frame_4, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.frame_5 = QFrame(self.left_menu_widget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_5)
        self.gridLayout_6.setSpacing(7)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame_5)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_6.addWidget(self.label_2, 0, 1, 1, 1)

        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout_6.addWidget(self.label_3, 1, 1, 1, 1)

        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout_6.addWidget(self.label_4, 2, 1, 1, 1)

        self.label_15 = QLabel(self.frame_5)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setMaximumSize(QSize(24, 24))
        self.label_15.setPixmap(QPixmap(u":/icons/icons/settings.svg"))
        self.label_15.setScaledContents(True)

        self.gridLayout_6.addWidget(self.label_15, 0, 0, 1, 1)

        self.label_17 = QLabel(self.frame_5)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setMaximumSize(QSize(24, 24))
        self.label_17.setPixmap(QPixmap(u":/icons/icons/search.svg"))
        self.label_17.setScaledContents(True)

        self.gridLayout_6.addWidget(self.label_17, 2, 0, 1, 1)

        self.label_16 = QLabel(self.frame_5)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMaximumSize(QSize(24, 24))
        self.label_16.setPixmap(QPixmap(u":/icons/icons/info.svg"))
        self.label_16.setScaledContents(True)

        self.gridLayout_6.addWidget(self.label_16, 1, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame_5)


        self.horizontalLayout.addWidget(self.left_menu_widget)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.frame_2)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setFrameShape(QFrame.StyledPanel)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 7, 0, 7)
        self.frame_9 = QFrame(self.header_frame)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pushButton_6 = QPushButton(self.frame_9)
        self.pushButton_6.setObjectName(u"pushButton_6")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/align-center.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon5)
        self.pushButton_6.setIconSize(QSize(30, 30))

        self.horizontalLayout_4.addWidget(self.pushButton_6)

        self.label_5 = QLabel(self.frame_9)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_4.addWidget(self.label_5)


        self.horizontalLayout_3.addWidget(self.frame_9, 0, Qt.AlignLeft)

        self.frame_11 = QFrame(self.header_frame)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_11)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.frame_11)
        self.label_6.setObjectName(u"label_6")
        font = QFont()
        self.label_6.setFont(font)

        self.verticalLayout_5.addWidget(self.label_6, 0, Qt.AlignHCenter)


        self.horizontalLayout_3.addWidget(self.frame_11)

        self.frame_10 = QFrame(self.header_frame)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_5.setSpacing(7)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.pushButton_9 = QPushButton(self.frame_10)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(30, 30))
        self.pushButton_9.setMaximumSize(QSize(30, 30))
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon6)
        self.pushButton_9.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.pushButton_9)

        self.pushButton_8 = QPushButton(self.frame_10)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(30, 30))
        self.pushButton_8.setMaximumSize(QSize(30, 30))
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/maximize-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon7)
        self.pushButton_8.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.pushButton_8)

        self.pushButton_7 = QPushButton(self.frame_10)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(30, 30))
        self.pushButton_7.setMaximumSize(QSize(30, 30))
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon8)
        self.pushButton_7.setIconSize(QSize(24, 24))

        self.horizontalLayout_5.addWidget(self.pushButton_7)


        self.horizontalLayout_3.addWidget(self.frame_10, 0, Qt.AlignRight)


        self.verticalLayout_4.addWidget(self.header_frame)

        self.frame_7 = QFrame(self.frame_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_7)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.stackedWidget = QStackedWidget(self.frame_7)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setFont(font)
        self.percentage_chart = QWidget()
        self.percentage_chart.setObjectName(u"percentage_chart")
        self.verticalLayout_9 = QVBoxLayout(self.percentage_chart)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.frame_14 = QFrame(self.percentage_chart)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_14)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_8 = QLabel(self.frame_14)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_8, 0, Qt.AlignTop)


        self.verticalLayout_9.addWidget(self.frame_14, 0, Qt.AlignTop)

        self.frame_15 = QFrame(self.percentage_chart)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy)
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_15)
        self.gridLayout.setObjectName(u"gridLayout")

        self.verticalLayout_9.addWidget(self.frame_15)

        self.stackedWidget.addWidget(self.percentage_chart)
        self.temp_chart = QWidget()
        self.temp_chart.setObjectName(u"temp_chart")
        self.verticalLayout_8 = QVBoxLayout(self.temp_chart)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_17 = QFrame(self.temp_chart)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_17)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_9 = QLabel(self.frame_17)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_11.addWidget(self.label_9, 0, Qt.AlignTop)


        self.verticalLayout_8.addWidget(self.frame_17, 0, Qt.AlignTop)

        self.frame_16 = QFrame(self.temp_chart)
        self.frame_16.setObjectName(u"frame_16")
        sizePolicy.setHeightForWidth(self.frame_16.sizePolicy().hasHeightForWidth())
        self.frame_16.setSizePolicy(sizePolicy)
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_16)
        self.gridLayout_2.setObjectName(u"gridLayout_2")

        self.verticalLayout_8.addWidget(self.frame_16)

        self.stackedWidget.addWidget(self.temp_chart)
        self.nested_chart = QWidget()
        self.nested_chart.setObjectName(u"nested_chart")
        self.verticalLayout_14 = QVBoxLayout(self.nested_chart)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_19 = QFrame(self.nested_chart)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_19)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_10 = QLabel(self.frame_19)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_10, 0, Qt.AlignTop)


        self.verticalLayout_14.addWidget(self.frame_19)

        self.frame_18 = QFrame(self.nested_chart)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy)
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_18)
        self.gridLayout_3.setObjectName(u"gridLayout_3")

        self.verticalLayout_14.addWidget(self.frame_18)

        self.stackedWidget.addWidget(self.nested_chart)
        self.line_chart = QWidget()
        self.line_chart.setObjectName(u"line_chart")
        self.verticalLayout_16 = QVBoxLayout(self.line_chart)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.frame_21 = QFrame(self.line_chart)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_21)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_11 = QLabel(self.frame_21)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.label_11, 0, Qt.AlignTop)


        self.verticalLayout_16.addWidget(self.frame_21)

        self.frame_20 = QFrame(self.line_chart)
        self.frame_20.setObjectName(u"frame_20")
        sizePolicy.setHeightForWidth(self.frame_20.sizePolicy().hasHeightForWidth())
        self.frame_20.setSizePolicy(sizePolicy)
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_20)
        self.gridLayout_4.setObjectName(u"gridLayout_4")

        self.verticalLayout_16.addWidget(self.frame_20)

        self.stackedWidget.addWidget(self.line_chart)
        self.bar_chart = QWidget()
        self.bar_chart.setObjectName(u"bar_chart")
        self.bar_chart.setStyleSheet(u"")
        self.verticalLayout_18 = QVBoxLayout(self.bar_chart)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.frame_23 = QFrame(self.bar_chart)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_23)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_12 = QLabel(self.frame_23)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font)
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_12, 0, Qt.AlignTop)


        self.verticalLayout_18.addWidget(self.frame_23)

        self.frame_22 = QFrame(self.bar_chart)
        self.frame_22.setObjectName(u"frame_22")
        sizePolicy.setHeightForWidth(self.frame_22.sizePolicy().hasHeightForWidth())
        self.frame_22.setSizePolicy(sizePolicy)
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_22)
        self.gridLayout_5.setObjectName(u"gridLayout_5")

        self.verticalLayout_18.addWidget(self.frame_22)

        self.stackedWidget.addWidget(self.bar_chart)

        self.verticalLayout_7.addWidget(self.stackedWidget)


        self.verticalLayout_4.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.frame_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_12 = QFrame(self.frame_8)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_12)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_7 = QLabel(self.frame_12)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_6.addWidget(self.label_7)


        self.horizontalLayout_6.addWidget(self.frame_12)

        self.frame_13 = QFrame(self.frame_8)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.size_grip = QFrame(self.frame_13)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setGeometry(QRect(130, 80, 120, 80))
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.frame_13)


        self.verticalLayout_4.addWidget(self.frame_8)


        self.horizontalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_14.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Percentage Chart", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Teamparature Chart", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Nested Donuts", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Line Chart", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Bar Chart", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"About Us", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.label_15.setText("")
        self.label_17.setText("")
        self.label_16.setText("")
        self.pushButton_6.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"DashBoard", None))
        self.pushButton_9.setText("")
        self.pushButton_8.setText("")
        self.pushButton_7.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Percantage Chart", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Temperature Bar Chart", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Nested Donut Chart", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Line  Chart", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Bar Chart", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Developed By Masum Billah Mishu", None))
    # retranslateUi

