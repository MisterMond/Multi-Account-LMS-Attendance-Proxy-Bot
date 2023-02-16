# Multi-Account-LMS-Attendance-Proxy-Bot
[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FMisterMond%2FMulti-Account-Attendance-Proxy-Bot&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=hits&edge_flat=false)](https://hits.seeyoufarm.com)

In one go, mark attendance on LMS from multiple accounts.

## Usage
This program auto-logins multiple accounts on LMS simultaneously using the credentials you provide in [credentials.json](https://github.com/MisterMond/Multi-Account-Attendance-Proxy-Bot/blob/main/credentials.json) and marks their attendance in the course you select using the attendance password you enter.

Run [bot.py](https://github.com/MisterMond/Multi-Account-LMS-Attendance-Proxy-Bot/blob/main/bot.py) as you would any python program.

eg.
```
python3 bot.py
```

![image](https://user-images.githubusercontent.com/125508084/219305818-ef5b1fbe-3203-4f5b-8661-39fcc4983b10.png)

![Screenshot](https://user-images.githubusercontent.com/125508084/219320548-49d7996e-c52c-4905-9f03-0d407a6aa1e1.png)

![image](https://user-images.githubusercontent.com/125508084/219306087-fd864bf1-ec5f-49fa-ab1a-fad1ccd6f68c.png)



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
