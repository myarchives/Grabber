import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow_Tracker(object):
    def setupUi(self, MainWindow_Tracker):
        MainWindow_Tracker.setObjectName("MainWindow")
        MainWindow_Tracker.resize(794, 351)
        MainWindow_Tracker.setMinimumSize(QtCore.QSize(794, 351))
        MainWindow_Tracker.setMaximumSize(QtCore.QSize(794, 351))
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
        MainWindow_Tracker.setPalette(palette)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Assets/grabbericon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow_Tracker.setWindowIcon(icon)
        MainWindow_Tracker.setIconSize(QtCore.QSize(30, 30))
        MainWindow_Tracker.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow_Tracker)
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
        self.banner.setPixmap(QtGui.QPixmap("Assets/tracker.png"))
        self.banner.setScaledContents(True)
        self.banner.setObjectName("banner")
        self.horizontalLayout_header.addWidget(self.banner)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(140, 240, 381, 31))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(540, 240, 89, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 240, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow_Tracker.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow_Tracker)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 794, 22))
        self.menubar.setObjectName("menubar")
        MainWindow_Tracker.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow_Tracker)
        self.statusbar.setObjectName("statusbar")
        MainWindow_Tracker.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow_Tracker)
        QtCore.QMetaObject.connectSlotsByName(MainWindow_Tracker)

    def retranslateUi(self, MainWindow_Tracker):
        _translate = QtCore.QCoreApplication.translate
        MainWindow_Tracker.setWindowTitle(_translate("MainWindow", "Grabber"))
        self.header.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" color:#121111;\">Tracker<br/></span><span style=\" font-size:16pt; color:#121111;\">Powered by Python and Selenium</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Track"))
        self.label.setText(_translate("MainWindow", "Product Url"))

class MainWindow_Tracker(QtWidgets.QMainWindow, Ui_MainWindow_Tracker):
    def __init__(self, parent=None):
        super(MainWindow_Tracker, self).__init__(parent)
        self.setupUi(self)