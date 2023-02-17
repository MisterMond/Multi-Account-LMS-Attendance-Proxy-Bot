from selenium.webdriver.common.by import By
from selenium import webdriver
import threading
import os.path
import time
import json

event=threading.Event()

def get_url():
    global url

    with open(os.path.join(path, 'courses.json')) as json_file:
        course_url=[]

        print("----------------------------------------------------------------------")
        data=json.load(json_file)
        i=1
        for course in data['courses']:
            print(f"|{i}.{course['name']}|", end="\t")
            course_url.append(course['url'])
            i=i+1

        print("\n----------------------------------------------------------------------")
        selection=int(input("Enter course sno: "))
        url=course_url[selection-1]


def prepare_and_fire_bot():
    with open(os.path.join(path, 'credentials.json')) as json_file:
        data=json.load(json_file)
        
        for account in data['accounts']:
            username=account['username']
            password=account['password']
            
            t=threading.Thread(target=bot, args=(username, password))
            t.start()


def bot(username, password):
    ######################################################################################
    #CHOOSE ONLY ONE WEB BROWSER THAT IS INSTALLED ON YOUR SYSTEM AND COMMENT OUT THE REST
    #driver=webdriver.Chrome()
    #driver=webdriver.Edge()
    driver=webdriver.Firefox()
    #driver=webdriver.Safari()
    ######################################################################################

    driver.get(url)

    #Auto login
    driver.find_element(By.NAME, 'username').send_keys(username)
    driver.find_element(By.NAME, 'password').send_keys(password)
    driver.find_element(By.ID, 'loginbtn').click()


    #Autofill attendance password
    event.wait()
    driver.find_element(By.NAME, 'qrpass').send_keys(attendance_password)
    driver.find_elements(By.CLASS_NAME, 'btn-secondary')[1].click()
    
    time.sleep(5)
    driver.close()
    

if __name__=="__main__":
    #Get path of local folder
    global path
    path=os.path.dirname(os.path.realpath(__file__))    

    #Get url of course
    get_url()

    #Ready LMS credentials and auto-login    
    prepare_and_fire_bot()        

    #Enter attendance password
    global attendance_password
    attendance_password=input('Enter attendance password after all attendance pages load: ')
    event.set()