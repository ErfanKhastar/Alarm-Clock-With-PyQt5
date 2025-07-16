# ⏰ Alarm Clock
A classic desktop alarm clock application created with Python. It features a user-friendly graphical interface built using PyQt5 and utilizes Pygame to play the alarm sound.

<br>

## ✨ Features
- **Intuitive Time Setting:** Easily set your alarm time using dropdown menus for hours, minutes, and AM/PM period.
- **Clear Controls:** Activate and deactivate the alarm with dedicated "Activate" and "Deactivate" buttons.
- **Live Countdown:** A real-time countdown timer shows you exactly how much time is left until the alarm goes off.
- **Sound Alert:** Plays an `alarm.mp3` sound file to wake you up when the time is reached. The sound is handled in a separate thread to keep the UI responsive.
- **Pop-up Notification:** Displays a "WAKE UP!!" message box when the alarm triggers.
- **Smart Scheduling:** If you set a time that has already passed for the current day, the alarm is automatically scheduled for the next day.
- **Automatic Reset:** The application state resets after the alarm goes off or is manually deactivated.

<br>

## 🛠️ Technologies Used
- **Programming Language:** `Python`
- **GUI Library:** `PyQt5`
- **Audio Playback:** `Pygame`

<br>

## 🚀 Getting Started
To run this application on your local machine, please follow the steps below.

### Prerequisites
You need to have Python installed. You will also need to install the `PyQt5` and `Pygame` libraries. You can install them using pip:
```bash
pip install PyQt5 pygame
```

### Installation & Running
Clone the project from GitHub to your local machine:
```bash
git clone https://github.com/ErfanKhastar/Alarm-Clock-With-PyQt5.git
cd Alarm-Clock-With-PyQt5
```

### How To Run
Open your terminal or command prompt in that directory.  
Run the application with the following command:
```bash
python main.py
```
