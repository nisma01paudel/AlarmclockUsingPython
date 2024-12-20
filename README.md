# Alarm Clock Application

This is a simple Alarm Clock application built using Python's Tkinter library. It allows users to set an alarm for a specific time, and when the time is reached, it will play a sound alert. The application also displays the current time in real-time and updates every second.

## Features
- **Real-time Clock**: Displays the current time in hours, minutes, and seconds in 24-hour format.
- **Alarm Set Feature**: Allows users to set an alarm for a specific time.
- **Sound Alert**: When the alarm time is reached, a sound is played to alert the user.
- **Graphical User Interface (GUI)**: Uses Tkinter for a simple, intuitive interface with color-coded labels and input fields.

## Requirements
- Python 3.x
- Tkinter (usually comes pre-installed with Python)
- `winsound` for playing the alarm sound (Windows-only)

## Installation

1. Clone or download the repository to your local machine.
2. Ensure that you have Python 3.x installed. You can download it from [here](https://www.python.org/downloads/).
3. If you're using a different operating system that does not support `winsound`, you may need to use another library to play sounds, such as `pygame` or `playsound`.
4. Run the script with the following command:

   ```bash
   python alarm_clock.py
