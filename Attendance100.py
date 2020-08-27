#Logical imports
from datetime import datetime
import smtplib
import time
import sys
import csv
import os

#--------------------------------------------------------------------------------------------------------------
#UI imports
import tkinter as tk
from tkinter import filedialog, Text

#--------------------------------------------------------------------------------------------------------------
#Logical Code
def send_mail(day, curr_time, link):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login('EMAIL_HERE', 'PASSWORD_HERE')

    sent_from = 'EMAIL_HERE'

    to = ['ANOTHER_EMAIL_HERE'] #You can add multiple of these.
    subject = day + ' Class Reminder' + ' for ' + curr_time
    body = 'User is attending online class at ' + link + \
            '. Join if you are having a class with him.'

    email_text = "Subject: {}\n\n{}".format(subject, body)

    server.sendmail(sent_from, to, email_text)
    server.quit()

def find_next_class(timetable_location, day):
    current_time = datetime.now().strftime("%H:%M")
    curr_time = time.strptime(current_time, "%H:%M")
    
    with open(timetable_location, 'r') as timetable:
        reader = csv.reader(timetable)
        for row in reader:
            class_time = time.strptime(str(row[0]), "%H:%M")
            
            if class_time >= curr_time and row[day+1] == "exit":
                print("No more classes for today.")
                exit()
            elif class_time >= curr_time and row[day+1] != "":
                print("Next Class at " + row[0])
                return class_time, row[day+1]
    
    print("Classes already over.")
    exit()

def attend_class(timetable_location):
    Weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
    day = datetime.today().weekday()
    print(Weekdays[day])

    while True:
        class_time, link = find_next_class(timetable_location, day) 
        while True:
            current_time = datetime.now().strftime("%H:%M")
            curr_time = time.strptime(current_time, "%H:%M")
            print("Current Time : " + current_time)

            if class_time == curr_time:
                print("Class at " + current_time)
                os.system("start "" " + link)
                print("Joined class at link : " + link)
                time.sleep(60)
                #send_mail(Weekdays[day], current_time, link)
                break

            time.sleep(60)

#--------------------------------------------------------------------------------------------------------------
#UI Code
root = tk.Tk()

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        apps = f.read()
        apps = apps.split(',')

if(len(apps) == 0):
    apps = ["","",""]

def addApp(type,extension,index):

    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir = "/",title = "Select File", filetypes=((type,extension),("all files","*.*")))
    apps[index] = filename
    
    for i in range(3):
        if(apps[i] == ""):
            INFO = tk.Label(frame, text = "Please Add all the 3 paths", bg = "red", fg = "black")
            INFO.pack()
            break

    show()

def showCSV():
    os.startfile(apps[2])

def final():
    saveFile()
    root.destroy()
    attend_class(apps[2])

def saveFile():
    if(len(apps) > 3):
        del apps[3:]
    with open('save.txt', 'w') as f:
        for app in apps:
            f.write(app + ',')

canvas = tk.Canvas(root,height = 400, width = 800, bg = "#ccccff")
canvas.pack()

frame = tk.Frame(root, bg = "#e6e6ff")
frame.place(relwidth = 0.8, relheight = 0.8,relx = 0.1, rely = 0.1)

pythonFile = tk.Button(root, text="Python File", padx=10, pady =5, fg="white", bg="#263D42", command = lambda: addApp("executables","*.exe",0))
pythonFile.pack()

PythonScript = tk.Button(root, text="Python Script", padx=10, pady=5, fg="white", bg="#263D42",command = lambda: addApp("Script File","*.py",1))
PythonScript.pack()

CSV_File = tk.Button(root, text="CSV file", padx=10, pady=5, fg="white", bg="#263D42", command = lambda: addApp("CSV file","*.csv",2))
CSV_File.pack()

CSV_check = tk.Button(root, text="Check CSV", padx=10, pady=5, fg="white", bg="#263D42", command = showCSV)
CSV_check.pack()

Proceed = tk.Button(root, text="Attend Class", padx=10, pady=5, fg="white", bg="#263D42", command = final)
Proceed.pack()

def show():
    for i in range(3):
        if(apps[i] == ""):
            INFO = tk.Label(frame, text = "Please Add all the 3 paths", bg = "red", fg = "black")
            INFO.pack()
            break
    for app in apps:
        label = tk.Label(frame, text = app, bg = "#b3ffb3")
        label.pack()

show()

root.mainloop()
saveFile()