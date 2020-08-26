from datetime import datetime
import smtplib
import time
import sys
import csv
import os

def send_mail(day, curr_time, link):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login('EMAIL_HERE', 'PASSWORD_HERE')

    sent_from = 'EMAIL_HERE'

    to = ['ANOTHER_EMAIL_HERE'] #You can add multiple of these.
    subject = day + ' Class Reminder' + ' for ' + curr_time
    body = 'Kartik is attending online class at ' + link + \
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
            elif class_time >= curr_time and row[day+1] != "NIL":
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

if __name__ == "__main__":
    attend_class(sys.argv[1])