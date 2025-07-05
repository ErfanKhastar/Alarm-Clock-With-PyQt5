from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QPushButton, QComboBox, QMessageBox
from PyQt5.QtCore import QTimer, QTime, QDateTime, QDate
from PyQt5 import uic
import sys
import time
from threading import Thread
import pygame


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load The UI File
        uic.loadUi("alarm.ui", self)
        self.setWindowTitle("Alarm Clock!")

        # Define Our Widgets
        self.pic = self.findChild(QLabel, "pic_label")
        self.alarmL = self.findChild(QLabel, "alarm_label")
        self.hoursL = self.findChild(QLabel, "hours_label")
        self.minutesL = self.findChild(QLabel, "minutes_label")
        self.periodL = self.findChild(QLabel, "period_label")
        self.countdownL = self.findChild(QLabel, "countdown_label")
        self.hoursC = self.findChild(QComboBox, "hours_comboBox")
        self.minutesC = self.findChild(QComboBox, "minutes_comboBox")
        self.periodC = self.findChild(QComboBox, "period_comboBox")
        self.AC = self.findChild(QPushButton, "activate_pushButton")
        self.DC = self.findChild(QPushButton, "deactivate_pushButton")

        # Add Item To The ComboBox
        self.hoursC.addItems(str(f"{i:02}") for i in range(0, 13))
        self.minutesC.addItems(str(f"{i:02}") for i in range(0, 60))
        self.periodC.addItems(["AM", "PM"])

        # Click The Button
        self.DC.clicked.connect(self.stop)
        self.AC.clicked.connect(self.run)

        # Disable The Deactivate Button
        self.DC.setEnabled(False)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_remaining_time)
        self.alarm_time = None
        self.alarm_active = False
        self.stop_alarm_sound = False
        pygame.mixer.init()

        # Show The App
        self.show()

    # Activate The Alarm
    def run(self):
        # Get The Text From ComboBoxes
        hour = int(self.hoursC.currentText())
        minutes = int(self.minutesC.currentText())
        period = self.periodC.currentText()

        if period == "PM" and hour != 12:
            hour += 12
        elif period == "AM" and hour == 12:
            hour = 0

        now = QDateTime.currentDateTime()
        alarm_date = QDate.currentDate()
        self.alarm_time = QDateTime(alarm_date, QTime(hour, minutes))

        if self.alarm_time <= now:
            self.alarm_time = self.alarm_time.addDays(1)

        self.alarm_active = True
        self.AC.setEnabled(False)
        self.DC.setEnabled(True)
        self.timer.start(1000)

        self.update_remaining_time()

    # Deactivate The Alarm
    def stop(self):
        self.alarm_active = False
        self.alarm_time = None
        self.stop_alarm_sound = True
        pygame.mixer.music.stop()
        self.AC.setEnabled(True)
        self.DC.setEnabled(False)
        self.countdownL.setText("00:00")
        self.timer.stop()
        
    # Remaining Time
    def update_remaining_time(self):
        if self.alarm_active:
            now = QDateTime.currentDateTime()
            remaining_seconds = now.secsTo(self.alarm_time)

            if remaining_seconds <= 0:
                self.play_alarm()
                return

            hours = remaining_seconds // 3600
            minutes = (remaining_seconds % 3600) // 60
            seconds = remaining_seconds % 60

            self.countdownL.setText(f"{hours:02}:{minutes:02}:{seconds:02}")

    # Play Alarm
    def play_alarm(self):
        def play_sound():
            self.stop_alarm_sound = False
            pygame.mixer.music.load("alarm.mp3")
            pygame.mixer.music.play(-1)

            start_time = time.time()

            while time.time() - start_time < 3:
                if self.stop_alarm_sound:
                    pygame.mixer.music.stop()
                    return
                time.sleep(0.1)
            pygame.mixer.music.stop()

        Thread(target=play_sound, daemon=True).start()
        QMessageBox.information(self, "Alarm", "WAKE UP!!")
        self.stop()


# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
