from datetime import datetime
import smtplib
import time
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
    
Weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
day = datetime.today().weekday()
print(Weekdays[day])

end_time = time.strptime("17:10", "%H:%M")

while True:
    #Replace with COMPLETE path to attendance file below.
    with open(r'E:\Programming\Python\Attendance100\timetable.csv', 'r') as timetable:
        reader = csv.reader(timetable)
        
        for row in reader:    
            now = datetime.now()
            current_time = now.strftime("%H:%M")
            curr_time = time.strptime(current_time, "%H:%M")
            print("Current Time =", current_time)
            if (curr_time > end_time):
                print("No classes for now.")
                exit()
            link = ""

            class_time = time.strptime(str(row[0]), "%H:%M")
            
            if class_time == curr_time:
                if row[day+1] == "exit":
                    print("End of the day. :D")
                    exit()
                elif row[day+1] == "NIL":
                    time.sleep(50 * 60)
                else:
                    link = row[day + 1]
                    print("Class at " + current_time)
                    os.system("start "" " + link)
                    print("Joined class at link : " + link)
                    #send_mail(Weekdays[day], current_time, link)
                    time.sleep(50 * 60)
            else:
                continue
            
    time.sleep(60)
