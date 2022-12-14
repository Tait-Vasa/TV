# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(700, 600)
        MainWindow.setMaximumSize(QtCore.QSize(700, 650))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.remote_Label = QtWidgets.QLabel(self.centralwidget)
        self.remote_Label.setGeometry(QtCore.QRect(110, 430, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.remote_Label.setFont(font)
        self.remote_Label.setScaledContents(True)
        self.remote_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.remote_Label.setWordWrap(True)
        self.remote_Label.setIndent(1)
        self.remote_Label.setObjectName("remote_Label")
        self.remote_line1 = QtWidgets.QFrame(self.centralwidget)
        self.remote_line1.setGeometry(QtCore.QRect(70, 60, 21, 431))
        self.remote_line1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.remote_line1.setLineWidth(10)
        self.remote_line1.setFrameShape(QtWidgets.QFrame.VLine)
        self.remote_line1.setObjectName("remote_line1")
        self.remote_line2 = QtWidgets.QFrame(self.centralwidget)
        self.remote_line2.setGeometry(QtCore.QRect(230, 60, 21, 431))
        self.remote_line2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.remote_line2.setLineWidth(10)
        self.remote_line2.setFrameShape(QtWidgets.QFrame.VLine)
        self.remote_line2.setObjectName("remote_line2")
        self.remote_line3 = QtWidgets.QFrame(self.centralwidget)
        self.remote_line3.setGeometry(QtCore.QRect(80, 50, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.remote_line3.setFont(font)
        self.remote_line3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.remote_line3.setLineWidth(10)
        self.remote_line3.setFrameShape(QtWidgets.QFrame.HLine)
        self.remote_line3.setObjectName("remote_line3")
        self.remote_line4 = QtWidgets.QFrame(self.centralwidget)
        self.remote_line4.setGeometry(QtCore.QRect(80, 470, 161, 31))
        self.remote_line4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.remote_line4.setLineWidth(10)
        self.remote_line4.setFrameShape(QtWidgets.QFrame.HLine)
        self.remote_line4.setObjectName("remote_line4")
        self.channel_label = QtWidgets.QLabel(self.centralwidget)
        self.channel_label.setGeometry(QtCore.QRect(130, 140, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.channel_label.setFont(font)
        self.channel_label.setAlignment(QtCore.Qt.AlignCenter)
        self.channel_label.setObjectName("channel_label")
        self.tv_label = QtWidgets.QLabel(self.centralwidget)
        self.tv_label.setGeometry(QtCore.QRect(470, 50, 51, 61))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.tv_label.setFont(font)
        self.tv_label.setObjectName("tv_label")
        self.tv_line3 = QtWidgets.QFrame(self.centralwidget)
        self.tv_line3.setGeometry(QtCore.QRect(330, 100, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tv_line3.setFont(font)
        self.tv_line3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tv_line3.setLineWidth(12)
        self.tv_line3.setFrameShape(QtWidgets.QFrame.HLine)
        self.tv_line3.setObjectName("tv_line3")
        self.tv_line1 = QtWidgets.QFrame(self.centralwidget)
        self.tv_line1.setGeometry(QtCore.QRect(320, 110, 31, 221))
        self.tv_line1.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tv_line1.setLineWidth(12)
        self.tv_line1.setFrameShape(QtWidgets.QFrame.VLine)
        self.tv_line1.setObjectName("tv_line1")
        self.tv_line2 = QtWidgets.QFrame(self.centralwidget)
        self.tv_line2.setGeometry(QtCore.QRect(640, 110, 31, 221))
        self.tv_line2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tv_line2.setLineWidth(12)
        self.tv_line2.setFrameShape(QtWidgets.QFrame.VLine)
        self.tv_line2.setObjectName("tv_line2")
        self.tv_line4 = QtWidgets.QFrame(self.centralwidget)
        self.tv_line4.setGeometry(QtCore.QRect(330, 310, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.tv_line4.setFont(font)
        self.tv_line4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.tv_line4.setLineWidth(12)
        self.tv_line4.setFrameShape(QtWidgets.QFrame.HLine)
        self.tv_line4.setObjectName("tv_line4")
        self.power_Button = QtWidgets.QPushButton(self.centralwidget)
        self.power_Button.setGeometry(QtCore.QRect(110, 80, 101, 28))
        self.power_Button.setObjectName("power_Button")
        self.chandown_button = QtWidgets.QPushButton(self.centralwidget)
        self.chandown_button.setGeometry(QtCore.QRect(190, 140, 31, 31))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.chandown_button.setFont(font)
        self.chandown_button.setObjectName("chandown_button")
        self.chanup_button = QtWidgets.QPushButton(self.centralwidget)
        self.chanup_button.setGeometry(QtCore.QRect(100, 140, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.chanup_button.setFont(font)
        self.chanup_button.setObjectName("chanup_button")
        self.volup_button = QtWidgets.QPushButton(self.centralwidget)
        self.volup_button.setGeometry(QtCore.QRect(100, 200, 31, 28))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.volup_button.setFont(font)
        self.volup_button.setObjectName("volup_button")
        self.voldown_button = QtWidgets.QPushButton(self.centralwidget)
        self.voldown_button.setGeometry(QtCore.QRect(190, 200, 31, 28))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.voldown_button.setFont(font)
        self.voldown_button.setObjectName("voldown_button")
        self.volume_label = QtWidgets.QLabel(self.centralwidget)
        self.volume_label.setGeometry(QtCore.QRect(130, 200, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.volume_label.setFont(font)
        self.volume_label.setAlignment(QtCore.Qt.AlignCenter)
        self.volume_label.setObjectName("volume_label")
        self.mute_button = QtWidgets.QPushButton(self.centralwidget)
        self.mute_button.setGeometry(QtCore.QRect(120, 240, 81, 28))
        self.mute_button.setObjectName("mute_button")
        self.tv_output = QtWidgets.QLabel(self.centralwidget)
        self.tv_output.setGeometry(QtCore.QRect(346, 182, 291, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.tv_output.setFont(font)
        self.tv_output.setAlignment(QtCore.Qt.AlignCenter)
        self.tv_output.setObjectName("tv_output")
        self.volume_output = QtWidgets.QLabel(self.centralwidget)
        self.volume_output.setGeometry(QtCore.QRect(530, 140, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setItalic(True)
        self.volume_output.setFont(font)
        self.volume_output.setText("")
        self.volume_output.setAlignment(QtCore.Qt.AlignCenter)
        self.volume_output.setObjectName("volume_output")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 700, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "VaKun Remote"))
        self.remote_Label.setText(_translate("MainWindow", "VaKun"))
        self.channel_label.setText(_translate("MainWindow", "Channel"))
        self.tv_label.setText(_translate("MainWindow", "TV"))
        self.power_Button.setText(_translate("MainWindow", "Power"))
        self.chandown_button.setText(_translate("MainWindow", "v"))
        self.chanup_button.setText(_translate("MainWindow", "^"))
        self.volup_button.setText(_translate("MainWindow", "+"))
        self.voldown_button.setText(_translate("MainWindow", "-"))
        self.volume_label.setText(_translate("MainWindow", "Volume"))
        self.mute_button.setText(_translate("MainWindow", "Mute"))
        self.tv_output.setText(_translate("MainWindow", "Power Off"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
