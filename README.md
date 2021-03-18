# Attendance100
Automation for scheduled zoom meetings.

### Features
* Automatically opens scheduled zoom meetings where schedule is saved in a csv file.
* Can send email notifications about meetings that have started and joined by the script.

### Setup (for Windows)
1. Download & Install Python from [here](https://www.python.org/ftp/python/3.8.5/python-3.8.5.exe).
1. Fill the zoom meeting links in ```timetable.csv```.

### Usage

Run ```Attendance100.py```.

### Notes
* It would be better if zoom application is logged in already so that it doesn't ask for login credentials on joining the link.
* ```timetable.csv``` column number 1 to 6 denote Monday to Saturday.
* Days where schedule is over early, should end with ```exit``` in ```timetable.csv```. (See timetable.csv for reference)
* If the classes for the day are already over then the script would exit immediately after printing a message which says so.
* Code for email notification is commented out for ease of use to users. Anyone interested can uncomment it and fill in his mail server login credentials.

### Future
* Might update with more advanced features.
* Open to contributions & pull requests.
