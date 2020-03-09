#! /usr/bin/python3

import tkinter # note that module name has changed from Tkinter in Python 2 to tkinter in Python 3
from tkinter import Label,Canvas
mainwindow = tkinter.Tk()
mainwindow.title = "Alarmclock"
mainwindow.mainloop()
"""
from crontab import CronTab

cron = CronTab(user=True)

job  = cron.new(command='python3 /home/fr3gs/ownCloud/projects/alarmclock/main.py')
job.minute.on(21)
job.enable()
cron.write()
#
for job in cron:
    print(job)
    cron.remove( job )
cron.write()
"""