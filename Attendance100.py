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
# apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        temp = f.read()
        apps = temp.split(',')

if(len(apps) == 0):
    apps = [""]

def addApp(type,extension):

    for widget in frame.winfo_children():
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir = "/",title = "Select File", filetypes=((type,extension),("all files","*.*")))
    apps[0] = filename

    show()

def showCSV():
    if(apps[0] != ""):
        os.startfile(apps[0])

def final():
    saveFile()
    root.destroy()
    attend_class(apps[0])

def saveFile():
    if(len(apps) > 1):
        del apps[1:]
    with open('save.txt', 'w') as f:
        for app in apps:
            f.write(app + ',')

canvas = tk.Canvas(root,height = 100, width = 600, bg = "#ccccff")
canvas.pack()

frame = tk.Frame(root, bg = "#e6e6ff")
frame.place(relwidth = 0.8, relheight = 0.3,relx = 0.1, rely = 0.1)

CSV_File = tk.Button(root, text="Add Timetable", padx=5, pady=2, fg="white", bg="#263D42", command = lambda: addApp("CSV file","*.csv"))
CSV_File.pack()

CSV_check = tk.Button(root, text="Check CSV", padx=5, pady=2, fg="white", bg="#263D42", command = showCSV)
CSV_check.pack()
CSV_check.place(height=30, width=70)

Proceed = tk.Button(root, text="Automate", padx=5, pady=2, fg="white", bg="#263D42", command = final)
Proceed.pack()

def show():
    # print(apps)
    for i in range(len(apps)-1):
        if(apps[i] == ""):
            INFO = tk.Label(frame, text = "Please add a timetable", bg = "red", fg = "black")
            INFO.pack()
            break
    for i in range(len(apps)-1):
        label = tk.Label(frame, text = apps[i], bg = "#b3ffb3")
        label.pack()

show()
root.resizable(0, 0)
root.mainloop()
saveFile()