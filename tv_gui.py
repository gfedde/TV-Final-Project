# Form implementation generated from reading ui file 'tv_gui.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 850)
        MainWindow.setMinimumSize(QtCore.QSize(750, 850))
        MainWindow.setMaximumSize(QtCore.QSize(750, 850))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.push_power = QtWidgets.QPushButton(parent=self.centralwidget)
        self.push_power.setGeometry(QtCore.QRect(10, 10, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.push_power.setFont(font)
        self.push_power.setObjectName("push_power")
        self.push_mute = QtWidgets.QPushButton(parent=self.centralwidget)
        self.push_mute.setGeometry(QtCore.QRect(620, 10, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.push_mute.setFont(font)
        self.push_mute.setObjectName("push_mute")
        self.current_channel_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.current_channel_label.setGeometry(QtCore.QRect(330, 30, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.current_channel_label.setFont(font)
        self.current_channel_label.setObjectName("current_channel_label")
        self.channel1_push = QtWidgets.QPushButton(parent=self.centralwidget)
        self.channel1_push.setGeometry(QtCore.QRect(200, 280, 81, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.channel1_push.setFont(font)
        self.channel1_push.setObjectName("channel1_push")
        self.volume_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.volume_label.setGeometry(QtCore.QRect(400, 210, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.volume_label.setFont(font)
        self.volume_label.setObjectName("volume_label")
        self.channel2_push = QtWidgets.QPushButton(parent=self.centralwidget)
        self.channel2_push.setGeometry(QtCore.QRect(330, 280, 81, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.channel2_push.setFont(font)
        self.channel2_push.setObjectName("channel2_push")
        self.channel3_push = QtWidgets.QPushButton(parent=self.centralwidget)
        self.channel3_push.setGeometry(QtCore.QRect(460, 280, 81, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.channel3_push.setFont(font)
        self.channel3_push.setObjectName("channel3_push")
        self.channel4_push = QtWidgets.QPushButton(parent=self.centralwidget)
        self.channel4_push.setGeometry(QtCore.QRect(200, 400, 81, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.channel4_push.setFont(font)
        self.channel4_push.setObjectName("channel4_push")
        self.channel5_push = QtWidgets.QPushButton(parent=self.centralwidget)
        self.channel5_push.setGeometry(QtCore.QRect(330, 400, 81, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.channel5_push.setFont(font)
        self.channel5_push.setObjectName("channel5_push")
        self.channel6_push = QtWidgets.QPushButton(parent=self.centralwidget)
        self.channel6_push.setGeometry(QtCore.QRect(460, 400, 81, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.channel6_push.setFont(font)
        self.channel6_push.setObjectName("channel6_push")
        self.channel9_push = QtWidgets.QPushButton(parent=self.centralwidget)
        self.channel9_push.setGeometry(QtCore.QRect(460, 520, 81, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.channel9_push.setFont(font)
        self.channel9_push.setObjectName("channel9_push")
        self.channel8_push = QtWidgets.QPushButton(parent=self.centralwidget)
        self.channel8_push.setGeometry(QtCore.QRect(330, 520, 81, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.channel8_push.setFont(font)
        self.channel8_push.setObjectName("channel8_push")
        self.channel7_push = QtWidgets.QPushButton(parent=self.centralwidget)
        self.channel7_push.setGeometry(QtCore.QRect(200, 520, 81, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.channel7_push.setFont(font)
        self.channel7_push.setObjectName("channel7_push")
        self.volumeup_push = QtWidgets.QPushButton(parent=self.centralwidget)
        self.volumeup_push.setGeometry(QtCore.QRect(100, 620, 221, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.volumeup_push.setFont(font)
        self.volumeup_push.setObjectName("volumeup_push")
        self.channelup_push = QtWidgets.QPushButton(parent=self.centralwidget)
        self.channelup_push.setGeometry(QtCore.QRect(410, 620, 221, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.channelup_push.setFont(font)
        self.channelup_push.setObjectName("channelup_push")
        self.channeldown_push = QtWidgets.QPushButton(parent=self.centralwidget)
        self.channeldown_push.setGeometry(QtCore.QRect(410, 710, 221, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.channeldown_push.setFont(font)
        self.channeldown_push.setObjectName("channeldown_push")
        self.volumedown_push = QtWidgets.QPushButton(parent=self.centralwidget)
        self.volumedown_push.setGeometry(QtCore.QRect(100, 710, 221, 71))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.volumedown_push.setFont(font)
        self.volumedown_push.setObjectName("volumedown_push")
        self.image = QtWidgets.QLabel(parent=self.centralwidget)
        self.image.setGeometry(QtCore.QRect(230, 80, 311, 111))
        self.image.setText("")
        self.image.setPixmap(QtGui.QPixmap("../../Desktop/Assignments/abc_logo.jpg"))
        self.image.setScaledContents(True)
        self.image.setObjectName("image")
        self.volume_slider = QtWidgets.QSlider(parent=self.centralwidget)
        self.volume_slider.setGeometry(QtCore.QRect(89, 220, 271, 22))
        self.volume_slider.setMaximum(9)
        self.volume_slider.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.volume_slider.setTickPosition(QtWidgets.QSlider.TickPosition.TicksBelow)
        self.volume_slider.setObjectName("volume_slider")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 750, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Television"))
        self.push_power.setText(_translate("MainWindow", "Power"))
        self.push_mute.setText(_translate("MainWindow", "Mute"))
        self.current_channel_label.setText(_translate("MainWindow", "Channel"))
        self.channel1_push.setText(_translate("MainWindow", "1"))
        self.volume_label.setText(_translate("MainWindow", "Volume"))
        self.channel2_push.setText(_translate("MainWindow", "2"))
        self.channel3_push.setText(_translate("MainWindow", "3"))
        self.channel4_push.setText(_translate("MainWindow", "4"))
        self.channel5_push.setText(_translate("MainWindow", "5"))
        self.channel6_push.setText(_translate("MainWindow", "6"))
        self.channel9_push.setText(_translate("MainWindow", "9"))
        self.channel8_push.setText(_translate("MainWindow", "8"))
        self.channel7_push.setText(_translate("MainWindow", "7"))
        self.volumeup_push.setText(_translate("MainWindow", "Volume Up"))
        self.channelup_push.setText(_translate("MainWindow", "Channel Up"))
        self.channeldown_push.setText(_translate("MainWindow", "Channel Down"))
        self.volumedown_push.setText(_translate("MainWindow", "Volume Down"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
