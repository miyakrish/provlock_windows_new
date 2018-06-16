# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testFormMain.ui'
#
# Created: Tue May 22 15:08:26 2018
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!
import os

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1173, 558)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: #E6E6E6;")   

        # self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget = QtGui.QTabWidget(MainWindow)
        self.tabWidget.setAutoFillBackground(False)
        self.tabWidget.setStyleSheet("QTabWidget  QTabBar::tab{\n"
            "background-color: rgb(141, 141, 141);\n"
            "border-width: 2px;\n"
            "border-color: #aa0000;\n"
            "min-width: 12em;\n"
            "padding: 4px;\n"
            "color: rgb(255, 255, 255);\n"
            "height: 30px"
            "}\n"
            "\n"
            "QTabWidget  QTabBar::tab:!selected{\n"
            "background-color: #E6E6E6;\n"
            "font: 15px \"Roboto\";\n"
            "color: #606060;\n"
            "border-right: 1px solid #D3D3D3;\n"
            "}\n"
            "\n"
            "QTabWidget  QTabBar::tab:selected{\n"
            "background-color: #EEEEEE;\n"
            "font: 16px \"Roboto\";\n"
            "color: #606060;\n"
            "border-right: 1px solid #D3D3D3;\n"
            "text-align: center"
            "}\n"
            "\n"
            "") 

        # self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.corner_widget = QtGui.QWidget()
        self.corner_widget.setStyleSheet("min-width: 350px;float: right!important; \n")
        # self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout = QtGui.QHBoxLayout(self.corner_widget)
        # self.horizontalLayout.setSpacing(0)
        # self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        # self.bookMarkCombo = QtGui.QComboBox(self.centralwidget)
        self.bookMarkCombo = QtGui.QComboBox()
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bookMarkCombo.sizePolicy().hasHeightForWidth())
        # self.bookMarkCombo.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(10)
        font.setWeight(50)
        font.setItalic(False)
        font.setBold(False)
        self.bookMarkCombo.setFont(font)
        self.bookMarkCombo.setStyleSheet("background-color: rgb(255, 255, 255);\n"
            "font: 8pt \"Roboto\";\n"
            "border-width: 1px;\n"
            # "margin-left: 600px!important;\n"
            "\n"
            "position: absolute;\n"
            # "left: 100px;\n"
            "float: right!important; \n"
            "max-width: 300px!important;\n"
            "padding: 1px;\n"
            "height: 22px!important;\n"
            "border-color: rgb(170, 0, 0);\n"
            "color: #606060;")
        self.bookMarkCombo.setEditable(True)
        #self.bookMarkCombo.setCurrentText("")
        self.bookMarkCombo.setFrame(True)
        self.bookMarkCombo.setObjectName("bookMarkCombo")
        self.horizontalLayout.addWidget( self.bookMarkCombo)
        # self.label_provImage = QtGui.QLabel(self.centralwidget)
        self.label_provImage = QtGui.QLabel(self.centralwidget)
        self.label_provImage.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_provImage.sizePolicy().hasHeightForWidth())
        self.label_provImage.setSizePolicy(sizePolicy)
        #self.label_provImage.setMinimumSize(QtCore.QSize(100, 2000))
        self.label_provImage.setMaximumSize(QtCore.QSize(150, 3500))
        font = QtGui.QFont()
        self.label_provImage.setFont(font)
        self.label_provImage.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label_provImage.setStyleSheet("")
        self.label_provImage.setText("")
        self.label_provImage.setPixmap(QtGui.QPixmap("/icons/ProvLogoMain.png"))
        self.label_provImage.show()
        self.label_provImage.setAlignment(QtCore.Qt.AlignCenter)
        self.label_provImage.setWordWrap(True)
        self.label_provImage.setObjectName("label_provImage")
        self.label_provImage.setScaledContents(True)
        # self.horizontalLayout.addWidget(self.label_provImage)
        # self.Quit = QtGui.QPushButton(self.centralwidget)
        # self.Quit = QtGui.QPushButton(self.centralwidget)
        # self.Quit = QtGui.QToolButton(self.centralwidget)
        # sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.Quit.sizePolicy().hasHeightForWidth())
        # self.Quit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setWeight(75)
        font.setBold(True)
        # self.Quit.setFont(font)
        # self.Quit.setStyleSheet("QToolButton#Pressed{\n"
        #     "background: transparent;\n"
        #     "padding: 2px 2px!important;\n"
        #     "max-width: 10px!important;\n"
        #     "text-align: center;\n"
        #     "display: inline-block;\n"
        #     "}\n"
        #     "QToolButton#Quit:pressed {\n"
        #     "    border-style: inset;\n"
        #     "}\n"
        #     "\n"
        #     "")
        # self.Quit.setObjectName("Quit")
        # self.horizontalLayout.addWidget(self.Quit)

        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 1)
        # self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        
        self.tabWidget.setElideMode(QtCore.Qt.ElideMiddle)
        self.tabWidget.setObjectName("tabWidget")
        self.test_console = QtGui.QWidget()
        self.test_console.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.test_console.setObjectName("test_console")
        self.tabWidget.addTab(self.test_console, "")

        self.search_option = QtGui.QWidget()
        self.search_option.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.search_option.setObjectName("search_option")

        # self.tabWidget.setCornerWidget(self.Quit)
        self.formLayout = QtGui.QFormLayout(self.search_option)
        self.formLayout.setObjectName("formLayout")
        self.lineEdit = QtGui.QLineEdit(self.search_option)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setWeight(75)
        font.setItalic(False)
        font.setBold(False)
        self.lineEdit.setFont(font)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtGui.QFormLayout.SpanningRole, self.lineEdit)
        self.tabWidget.addTab(self.search_option, "")
        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)
        # MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1173, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        button_icon = QtGui.QPixmap(self.get_push_button_path())
        # self.Quit.setIcon(button_icon)

        self.retranslateUi(MainWindow)
        self.bookMarkCombo.setCurrentIndex(-1)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.tabWidget, QtCore.SIGNAL("currentChanged(int)"), self.tabWidget.setCurrentIndex)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.tabWidget.setCornerWidget(self.corner_widget)
        # self.tabWidget.setCornerWidget(self.bookMarkCombo)
        # self.tabWidget.setCornerWidget(self.Quit)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        # self.Quit.setText(QtGui.QApplication.translate("MainWindow", "", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.test_console), QtGui.QApplication.translate("MainWindow", "Test Console", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit.setText(QtGui.QApplication.translate("MainWindow", "Look Here For Help", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.search_option), QtGui.QApplication.translate("MainWindow", "Search Option", None, QtGui.QApplication.UnicodeUTF8))
    
    def get_push_button_path(self):
        return "{}{}img{}cross.png".format(os.getcwd(),os.sep, os.sep)
