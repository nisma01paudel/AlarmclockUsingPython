# importing the required modules  
from tkinter import *  
import datetime as dt  
import time  
import threading  # For running alarm and clock simultaneously
import winsound as ws  
  
# defining the function for the alarm clock  
def alarm(setAlarmTimer):  
    while True:  
        time.sleep(1)  
        actualTime = dt.datetime.now()  
        currentTime = actualTime.strftime("%H : %M : %S")  
        currentDate = actualTime.strftime("%d / %m / %Y")  
        the_message = "Current Time: " + str(currentTime)  
        print(the_message)  
        if currentTime == setAlarmTimer:  
            ws.PlaySound("sound.wav", ws.SND_ASYNC)  
            break  
  
def getAlarmTime():  
    alarmSetTime = f"{hour.get()} : {minute.get()} : {second.get()}"  
    threading.Thread(target=alarm, args=(alarmSetTime,)).start()  # Run alarm in a separate thread
  
# Function to update the current time on the GUI
def updateClock():
    while True:
        actualTime = dt.datetime.now()
        currentTime = actualTime.strftime("%H : %M : %S")
        clockLabel.config(text="Current Time: " + currentTime)
        time.sleep(1)

# creating the GUI for the application  
guiWindow = Tk()  
guiWindow.title("The Alarm Clock")  
guiWindow.geometry("500x250")  
guiWindow.config(bg = "#D6AEDD")  
guiWindow.resizable(width = False, height = False)  
  
timeFormat = Label(  
    guiWindow,  
    text = "Remember to set time in 24-hour format!",  
    fg = "black",  
    bg = "#D6AEDD",  
    font = ("Arial", 15)  
    ).place(  
        x = 0,  
        y = 200  
        )  
  
clockLabel = Label(  
    guiWindow,  
    text = "",  
    font = ("Arial", 18),  
    bg = "#D6AEDD",  
    fg = "#4B0082"  
)  
clockLabel.place(x=140, y=10)  # Position for current time display
  
add_time = Label(  
    guiWindow,  
    text = "Hour     Minute     Second",  
    font = 60,  
    fg = "#4B0082",  
    bg = "#D6AEDD"  
    ).place(  
        x = 220,  
        y = 60  
        )  
  
setAlarm = Label(  
    guiWindow,  
    text = "Set Time for Alarm: ",  
    fg = "white",  
    bg = "#7B4E8D",  
    relief = "solid",  
    font = ("Helevetica", 13, "bold")  
    ).place(  
        x = 5,  
        y = 100  
        )  
  
hour = StringVar()  
minute = StringVar()  
second = StringVar()  
  
hourTime = Entry(  
    guiWindow,  
    textvariable = hour,  
    bg = "#FEFBD8",  
    width = 4,  
    font = (20)  
    ).place(  
        x = 220,  
        y = 103  
        )  
minuteTime = Entry(  
    guiWindow,  
    textvariable = minute,  
    bg = "#FEFBD8",  
    width = 4,  
    font = (20)  
    ).place(  
        x = 297,  
        y = 103  
        )  
secondTime = Entry(  
    guiWindow,  
    textvariable = second,  
    bg = "#FEFBD8",  
    width = 4,  
    font = (20)  
    ).place(  
        x = 390,  
        y = 103  
        )  
  
submit = Button(  
    guiWindow,  
    text = "Set The Alarm",  
    fg = "white",  
    bg = "#9B59B6",  
    width = 15,  
    command = getAlarmTime,  
    font = (20)  
    ).place(  
        x = 140,  
        y = 150  
        )  
  
# Start a thread to update the clock
threading.Thread(target=updateClock, daemon=True).start()

guiWindow.mainloop()
