import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import pyqtSlot

from specibuy_ui import MainWindow_Specibuy
from tracker_ui import MainWindow_Tracker

sys.path.insert(0, '/home/hakanohi/Projects/Grabber/Engine')
from product_info import scraperEvent


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 500)
        MainWindow.setMinimumSize(QtCore.QSize(800, 500))
        MainWindow.setMaximumSize(QtCore.QSize(800, 500))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 254, 254))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 254, 254))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 254, 254))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 254, 254))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        MainWindow.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Assets/grabbericon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QtCore.QSize(30, 30))
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(251, 245, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(251, 245, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(251, 245, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(251, 245, 245))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.centralwidget.setPalette(palette)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, 220, 721, 231))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_options = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_options.setContentsMargins(10, 10, 15, 10)
        self.horizontalLayout_options.setObjectName("horizontalLayout_options")
        self.verticalLayout_scraper = QtWidgets.QVBoxLayout()
        self.verticalLayout_scraper.setContentsMargins(5, 5, 5, 5)
        self.verticalLayout_scraper.setObjectName("verticalLayout_scraper")
        self.label_scraper = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_scraper.setMinimumSize(QtCore.QSize(141, 131))
        self.label_scraper.setMaximumSize(QtCore.QSize(141, 131))
        self.label_scraper.setText("")
        self.label_scraper.setPixmap(QtGui.QPixmap("Assets/scraper.png"))
        self.label_scraper.setScaledContents(True)
        self.label_scraper.setObjectName("label_scraper")
        self.verticalLayout_scraper.addWidget(self.label_scraper)
        self.pushButton_scraper = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_scraper.setFont(font)
        self.pushButton_scraper.setObjectName("pushButton_scraper")
        self.verticalLayout_scraper.addWidget(self.pushButton_scraper)
        self.horizontalLayout_options.addLayout(self.verticalLayout_scraper)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_options.addItem(spacerItem)
        self.verticalLayout_tracker = QtWidgets.QVBoxLayout()
        self.verticalLayout_tracker.setObjectName("verticalLayout_tracker")
        self.label_tracker = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_tracker.setMinimumSize(QtCore.QSize(141, 131))
        self.label_tracker.setMaximumSize(QtCore.QSize(141, 131))
        self.label_tracker.setText("")
        self.label_tracker.setPixmap(QtGui.QPixmap("Assets/tracker.png"))
        self.label_tracker.setScaledContents(True)
        self.label_tracker.setObjectName("label_tracker")
        self.verticalLayout_tracker.addWidget(self.label_tracker)
        self.pushButton_tracker = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_tracker.setFont(font)
        self.pushButton_tracker.setObjectName("pushButton_tracker")
        self.verticalLayout_tracker.addWidget(self.pushButton_tracker)
        self.horizontalLayout_options.addLayout(self.verticalLayout_tracker)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_options.addItem(spacerItem1)
        self.verticalLayout_specibuy = QtWidgets.QVBoxLayout()
        self.verticalLayout_specibuy.setObjectName("verticalLayout_specibuy")
        self.label_specibuy = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_specibuy.setMinimumSize(QtCore.QSize(141, 131))
        self.label_specibuy.setMaximumSize(QtCore.QSize(141, 131))
        self.label_specibuy.setText("")
        self.label_specibuy.setPixmap(QtGui.QPixmap("Assets/specibuy.png"))
        self.label_specibuy.setScaledContents(True)
        self.label_specibuy.setObjectName("label_specibuy")
        self.verticalLayout_specibuy.addWidget(self.label_specibuy)
        self.pushButton_specibuy = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        palette = QtGui.QPalette()
        self.pushButton_specibuy.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton_specibuy.setFont(font)
        self.pushButton_specibuy.setStyleSheet("")
        self.pushButton_specibuy.setObjectName("pushButton_specibuy")
        self.verticalLayout_specibuy.addWidget(self.pushButton_specibuy)
        self.horizontalLayout_options.addLayout(self.verticalLayout_specibuy)
        self.horizontalWidget_header = QtWidgets.QWidget(self.centralwidget)
        self.horizontalWidget_header.setGeometry(QtCore.QRect(39, 0, 721, 216))
        self.horizontalWidget_header.setAutoFillBackground(False)
        self.horizontalWidget_header.setStyleSheet("background: rgb(239, 239, 239)")
        self.horizontalWidget_header.setObjectName("horizontalWidget_header")
        self.horizontalLayout_header = QtWidgets.QHBoxLayout(self.horizontalWidget_header)
        self.horizontalLayout_header.setContentsMargins(20, 15, 25, 10)
        self.horizontalLayout_header.setObjectName("horizontalLayout_header")
        self.header = QtWidgets.QLabel(self.horizontalWidget_header)
        font = QtGui.QFont()
        font.setPointSize(32)
        self.header.setFont(font)
        self.header.setObjectName("header")
        self.horizontalLayout_header.addWidget(self.header)
        self.banner = QtWidgets.QLabel(self.horizontalWidget_header)
        self.banner.setMinimumSize(QtCore.QSize(241, 191))
        self.banner.setMaximumSize(QtCore.QSize(241, 191))
        self.banner.setText("")
        self.banner.setPixmap(QtGui.QPixmap("Assets/grabberbanner.png"))
        self.banner.setScaledContents(True)
        self.banner.setObjectName("banner")
        self.horizontalLayout_header.addWidget(self.banner)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Grabber"))
        self.pushButton_scraper.setText(_translate("MainWindow", "Scraper"))
        self.pushButton_tracker.setText(_translate("MainWindow", "Tracker"))
        self.pushButton_specibuy.setText(_translate("MainWindow", "Specibuy"))
        self.header.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#121111;\">GRABBER<br/></span><span style=\" font-size:16pt; color:#121111;\">Making Online Shopping Effortless</span></p></body></html>"))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_scraper.clicked.connect(self.scraperPopUp)
        self.pushButton_tracker.clicked.connect(self.trackerPopUp)
        self.pushButton_specibuy.clicked.connect(self.specibuyPopUp)

    @QtCore.pyqtSlot()
    def scraperPopUp(self):
        scraperEvent()

    def trackerPopUp(self):
        self.win_tracker = MainWindow_Tracker()
        self.win_tracker.show()

    def specibuyPopUp(self):
        self.win_specibuy = MainWindow_Specibuy()
        self.win_specibuy.show()
