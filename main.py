#!/usr/bin/python3
#import liraries
import tkinter # note that module name has changed from Tkinter in Python 2 to tkinter in Python 3
from tkinter import Label,Canvas
from urllib.request import urlopen
import base64
import io
import weather
import time
import os
if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')
#variables
weather = weather.check_weather()
degrees = str(weather['temp'])
time1 = ''
date1 = ''


#functions

def tick(): #function for updating clock
    global time1
    # get the current local time from the PC
    time2 = time.strftime('%H:%M:%S')
    date1 = time.strftime('%d/%m/%Y')
    # if time string has changed, update it
    if time2 != time1:
        time1 = time2
        lblClock.config(text=time2)
        lblDate.config(text=date1)
    # calls itself every 200 milliseconds
    # to update the time display as needed
    # could use >200 ms, but display gets jerky
    lblClock.after(200, tick)

#define main window
mainwindow = tkinter.Tk()
mainwindow.title = "Alarmclock"
mainwindow.geometry("800x480")
weatherFrame = tkinter.Frame(mainwindow)
weatherFrame.grid(column=0,row=0)

clockFrame = tkinter.Frame(mainwindow)
clockFrame.grid(column=1,row=0)

lblTemp = Label(weatherFrame, text= degrees + " graden", font=("Arial Bold", 20)) 
lblTemp.grid(column=0, row=0)

lblDescription = Label(weatherFrame, text= weather['description'], font=("Arial Bold", 20)) 
lblDescription.grid(column=0, row=1)

lblClock = Label(clockFrame, font=('times', 20, 'bold'), bg='green')
lblClock.pack()
#clock.grid(column=0,row=0)
lblDate = Label(clockFrame, font=('times', 20, 'bold'), bg='green')
lblDate.pack()

icon_url = "http://openweathermap.org/img/wn/" + weather['icon'] + "@2x.png"

image_byt = urlopen(icon_url).read()

image_b64 = base64.encodebytes(image_byt)

photo = tkinter.PhotoImage(data=image_b64)
iconCanvas = Canvas(weatherFrame, width=100, height=100)
iconCanvas.grid(column=1,row=0)
#iconCanvas.pack()
iconCanvas.create_image(50, 50, image=photo)

#functions



# Code to add widgets will go here...



#B = Button(top, text = "Hello", command = )
#B.place(x = 50,y = 50)
tick()
mainwindow.mainloop()