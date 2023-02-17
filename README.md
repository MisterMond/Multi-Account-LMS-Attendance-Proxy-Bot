# Multi-Account-LMS-Attendance-Proxy-Bot
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FMisterMond%2FMulti-Account-Attendance-Proxy-Bot&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

In one go, mark attendance on LMS from multiple accounts.


## Changelog
- 17/2/23  
Previously, there was a huge flaw that the bot would work only after the attendance password had been entered. If the pages were slow to load, the bot would've missed the 15 second window and failed to enter the correct password only to start the process all over again.  
Now, the bot auto-logins to LMS and asks for attendance password parallelly. Enter the password after you see that atttendance pages on all windows have loaded and attendance will be marked instantly. Simply replace the old [bot.py](https://github.com/MisterMond/Multi-Account-LMS-Attendance-Proxy-Bot/blob/main/bot.py) with the new one.


## Usage
This program auto-logins multiple accounts on LMS simultaneously using the credentials you provide in [credentials.json](https://github.com/MisterMond/Multi-Account-Attendance-Proxy-Bot/blob/main/credentials.json) and marks their attendance in the course you select using the attendance password you enter.

Run [bot.py](https://github.com/MisterMond/Multi-Account-LMS-Attendance-Proxy-Bot/blob/main/bot.py) as you would any python program.

eg.
```
python3 bot.py
```

![image](https://user-images.githubusercontent.com/125508084/219632802-9cca3b57-94d4-4ae9-bc0a-c53b09483986.png)


![Screenshot](https://user-images.githubusercontent.com/125508084/219702808-a59eb451-bd5a-4c87-ae52-2c59bbee540c.png)


## Installation & Setup
Prerequisite - python must be installed on your system.
1. Clone this repository.
2. Download the latest stable release of ChromeDriver from https://chromedriver.chromium.org/home for your operating system.
3. Unzip ChromeDriver into the local folder.  
The local directory structure should look like this:  
```
Multi-Account-LMS-Attendance-Proxy-Bot
|   bot.py
│   chromedriver
│   courses.json
|   credentials.json
│   README.md
```
4. Run this command in the terminal:
```
pip install selenium
```
#
Installation done! Now to set it up.

1. Go into [bot.py](https://github.com/MisterMond/Multi-Account-LMS-Attendance-Proxy-Bot/blob/main/bot.py) and choose a web browser that is installed on your system. Comment out the rest.

![image](https://user-images.githubusercontent.com/125508084/219166698-9f06ef70-d1b8-4058-abde-bdf9dfc94730.png)


2. Add all your courses to [courses.json](https://github.com/MisterMond/Multi-Account-Attendance-Proxy-Bot/blob/main/courses.json) in the following format:

![image](https://user-images.githubusercontent.com/125508084/219168647-00c549ff-d198-4f24-9f8e-e4d572936aee.png)

- Names can be anything that will help you identify the courses later on, but ***the urls must be links to "Lecture Attendance" pages***.

![image](https://user-images.githubusercontent.com/125508084/219171009-623cca2b-a639-490d-bda5-5e385860a820.png)

3. Add your LMS credentials, as well as credentials of your friends to [credentials.json](https://github.com/MisterMond/Multi-Account-Attendance-Proxy-Bot/blob/main/credentials.json) in the following format:

![image](https://user-images.githubusercontent.com/125508084/219173097-595b555d-6f55-4e9c-ab59-f7339c95c59d.png)

Setup done!

## Note
I made this program hastily and have only tested it on my native platform as a result.   
If you run into any issues, drop it here or send me an email at mistermond@pm.me and I'll get back to you.
