from PyQt6.QtWidgets import *
from tv_gui import *

class Television(QMainWindow, Ui_MainWindow):
    """
    A class representing details of a television object
    """
    MIN_VOLUME = 0
    MAX_VOLUME = 9
    MIN_CHANNEL = 0
    MAX_CHANNEL = 9
    def __init__(self):
        """
        Method to set default values of television object and connect gui buttons
        self.__status = Power status of television
        self.__muted = Mute status of television
        self.__volume = Current volume of television
        self._channel = Current channel of television
        """
        super().__init__()
        self.setupUi(self)
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
        self.push_power.clicked.connect(self.power)

        #Volume button connections
        self.volumeup_push.clicked.connect(self.volume_up)
        self.volumeup_push.clicked.connect(self.display_volume)
        self.volumedown_push.clicked.connect(self.volume_down)
        self.volumedown_push.clicked.connect(self.display_volume)
        self.push_mute.clicked.connect(self.mute)
        self.push_mute.clicked.connect(self.display_volume)

        #Channel button connections
        self.channelup_push.clicked.connect(self.channel_up)
        self.channelup_push.clicked.connect(self.display_channel)
        self.channeldown_push.clicked.connect(self.channel_down)
        self.channeldown_push.clicked.connect(self.display_channel)
        self.channel1_push.clicked.connect(self.channel_button1)
        self.channel1_push.clicked.connect(self.channel_image)
        self.channel1_push.clicked.connect(self.display_channel)
        self.channel2_push.clicked.connect(self.channel_button2)
        self.channel2_push.clicked.connect(self.channel_image)
        self.channel2_push.clicked.connect(self.display_channel)
        self.channel3_push.clicked.connect(self.channel_button3)
        self.channel3_push.clicked.connect(self.channel_image)
        self.channel3_push.clicked.connect(self.display_channel)
        self.channel4_push.clicked.connect(self.channel_button4)
        self.channel4_push.clicked.connect(self.channel_image)
        self.channel4_push.clicked.connect(self.display_channel)
        self.channel5_push.clicked.connect(self.channel_button5)
        self.channel5_push.clicked.connect(self.channel_image)
        self.channel5_push.clicked.connect(self.display_channel)
        self.channel6_push.clicked.connect(self.channel_button6)
        self.channel6_push.clicked.connect(self.channel_image)
        self.channel6_push.clicked.connect(self.display_channel)
        self.channel7_push.clicked.connect(self.channel_button7)
        self.channel7_push.clicked.connect(self.channel_image)
        self.channel7_push.clicked.connect(self.display_channel)
        self.channel8_push.clicked.connect(self.channel_button8)
        self.channel8_push.clicked.connect(self.channel_image)
        self.channel8_push.clicked.connect(self.display_channel)
        self.channel9_push.clicked.connect(self.channel_button9)
        self.channel9_push.clicked.connect(self.channel_image)
        self.channel9_push.clicked.connect(self.display_channel)

    def power(self) -> None:
        """
        Method to change power status of television
        :return: None
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Method to change mute status of television
        :return: None
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """
        Method to increase channel of television
        return: None
        """
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        Method to decrease channel of television
        :return: None
        """
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    # def volume_slide(self):
    #     self.volume_slider.valueChanged.connect(self.display_volume)

    def volume_up(self) -> None:
        """
        Method to increase volume of television
        :return: None
        """
        if self.__status:
            self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Method to decrease volume of television
        :return: None
        """
        if self.__status:
            self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def channel_button1(self) -> None:
        """
        Method to change channel to 1
        :return: none
        """
        self.__channel = 1
    def channel_button2(self) -> None:
        """
        Method to change channel to 2
        :return: none
        """
        self.__channel = 2
    def channel_button3(self) -> None:
        """
        Method to change channel to 3
        :return: none
        """
        self.__channel = 3
    def channel_button4(self) -> None:
        """
        Method to change channel to 4
        :return: none
        """
        self.__channel = 4
    def channel_button5(self) -> None:
        """
        Method to change channel to 5
        :return: none
        """
        self.__channel = 5
    def channel_button6(self) -> None:
        """
        Method to change channel to 6
        :return: none
        """
        self.__channel = 6
    def channel_button7(self) -> None:
        """
        Method to change channel to 7
        :return: none
        """
        self.__channel = 7
    def channel_button8(self) -> None:
        """
        Method to change channel to 8
        :return: none
        """
        self.__channel = 8
    def channel_button9(self) -> None:
        """
        Method to change channel to 9
        :return: none
        """
        self.__channel = 9
    def display_volume(self) -> None:
        """
        Method to display current volume of television
        """
        if self.__status:
            if self.__muted:
                self.__volume = 0
            volume_text = (
                f"Volume - {self.__volume}"
            )
            self.volume_label.setText(volume_text)
    def display_channel(self) -> None:
        """
        Method to display current channel of television
        :return:
        """
        if self.__status:
            channel_text = (
                f"Channel {self.__channel}"
            )
            self.current_channel_label.setText(channel_text)
            self.channel_image()

    def channel_image(self):
        """
        Method to change image on television
        :return: none
        """
        if self.__status:
            if self.__channel == 0:
                self.image.setPixmap(QtGui.QPixmap("cn_logo.jpg"))
            elif self.__channel == 1:
                self.image.setPixmap(QtGui.QPixmap("abc_logo.jpg"))
            elif self.__channel == 2:
                self.image.setPixmap(QtGui.QPixmap("cnn_logo.jpg"))
            elif self.__channel == 3:
                self.image.setPixmap(QtGui.QPixmap("fox_logo.jpg"))
            elif self.__channel == 4:
                self.image.setPixmap(QtGui.QPixmap("spongebob_logo.jpg"))
            elif self.__channel == 5:
                self.image.setPixmap(QtGui.QPixmap("scoobydoo_logo.jpg"))
            elif self.__channel == 6:
                self.image.setPixmap(QtGui.QPixmap("wowt_logo.jpg"))
            elif self.__channel == 7:
                self.image.setPixmap(QtGui.QPixmap("cbs_logo.jpg"))
            elif self.__channel == 8:
                self.image.setPixmap(QtGui.QPixmap("nbc_logo.jpg"))
            elif self.__channel == 9:
                self.image.setPixmap(QtGui.QPixmap("history_logo.jpg"))





