from concurrent.futures import thread
from enum import Flag
import fnmatch
from logging import exception
import sys
from unittest import result
from urllib import response
import webbrowser
import pyperclip
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import os
import random
from google_trans_new import google_translator
import smtplib
import pickle
from finalgui import Ui_MainWindow
from PyQt5 import QtCore , QtGui , QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt , QTimer , QTime , QDate
from PyQt5.uic import loadUiType
import requests
from bs4 import BeautifulSoup
from pywikihow import search_wikihow
import wolframalpha
import json
import requests
import cv2
import time
from playsound import playsound
from tmdbv3api import TMDb,Movie
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import spacy
from pytube import YouTube
from pyautogui import click, hotkey
from pyperclip import paste
from time import sleep
import pywhatkit
from chrome import ChromeAuto
from youtube import YouTubeAuto
from keyboard import press
from keyboard import press_and_release
from keyboard import write


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
now = datetime.datetime.now()
time = int(datetime.datetime.now().hour)

file = 'emails.pkl'
tmdb = TMDb()
movie = Movie()
flag = True

    # Function to speak
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

   
   
def wish(): 
    if time>=0 and time<=12:
        speak("Good morning sir . How may i help you")    
        print("Good morning sir . How may i help you")    
    elif time>=12 and time<=18:
        speak("Good afternoon sir . How may i help you") 
        print("Good afternoon sir . How may i help you") 
    else:
        speak("Good evening sir . How may i help you")         
        print("Good evening sir . How may i help you")         

    
def sendMail(to, message) :
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('eononpython@gmail.com' , 'cduqxicrcurnkrnv')
    server.sendmail('eononpython@gmail.com',to,message)
    server.close()
    print("email sent")
    speak("email sent")


def saveEmail(name , mail):
    name = name.replace(" ","")
    with open(file,'rb') as f:
        d=pickle.load(f)
    
    d[name] = mail
    with open(file,'wb') as f:
        pickle.dump(d,f)
    print("contact saved")
    speak("contact saved")



def weather(city):
    print("checking weather")
    speak("checking weather")
  
    api_key = "be3cafcd002ff28f28e13d069027ad03"
    url = "https://api.openweathermap.org/data/2.5/weather?" 
    comp_url = url+"appid="+api_key+"&q="+city
    res = requests.get(comp_url)
    if res.status_code == 200 :
        data = res.json()
        main = data['main']
        temperature = main['temp']
        humidity = main['humidity']
        pressure = main['pressure']
        report = data['weather']
        print(f"temperature = {temperature}")
        speak(f"temperature = {temperature}")
        print(f"humidity = {humidity}")
        speak(f"humidity = {humidity}")
        print(f"pressure = {pressure}")
        speak(f"pressure = {pressure}")
        print(f"weather report = {report[0]['description']}")
        speak(f"weather report = {report[0]['description']}")
    else:
        print("error in HTTP request")
        speak("error in HTTP request")


def news():     
                print("fetching news")    
                key = "74c9cf843b0540069744c9673159499a"
                url = "https://newsapi.org/v2/top-headlines?country=in&apiKey="+key
                news = requests.get(url).json()
                articles = news["articles"]

                my_articles = []
                my_news = ""
                for article in articles:
                    my_articles.append(article["title"])
                
                for i in range(5):
                    my_news = my_news + my_articles[i] + "\n"
                print(my_news)
                speak(my_news)


def movies():
    print("Getting top movies")
    speak("Getting top movies")
    tmdb.api_key= "4499c453c8970d7cf5dcbfdce1e17120"
    movie.api_key= "4499c453c8970d7cf5dcbfdce1e17120"
    popular = movie.popular()
    i = 0
                
    for p in popular:
        print(p.title)
        speak(p.title)
        i+=1
        if(i==5):
            break


    # Main class
class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.taskexecution()

    def taskexecution(self):
        
        while True:
            self.query = self.command().lower()

            if 'wikipedia' in self.query: #working fine
                speak("searching wikipedia")
                print("searching wikipedia")
                self.query = self.query.replace("wikipedia","")
                try:
                    results = wikipedia.summary(self.query, sentences=1)
                    speak("according to wikipedia")
                    print(results)
                    speak(results)

                except wikipedia.exceptions.WikipediaException as e:
                    print(e)
                    print(f"please specify which {self.query} do you want")
                    speak(f"please specify which {self.query} do you want")


            elif '.com ' in self.query:
                website=self.query.replace("open","")
                website=website.replace(" ","")
                webbrowser.open(website)   
                print(f"Opening {website}")
                speak(f"Opening {website}")
                print("entering chrome automation mode")
                speak("entering chrome automation mode")
                flag = True
                while flag :
                    query = self.command()
                    ChromeAuto(query)
                    if "exit" in query:
                        print("exiting chrome automation mode")
                        speak("exiting chrome automation mode")
                        break


        
            elif "youtube" in self.query:
                topic = self.query.replace("play ", "")
                topic = topic.replace(" on youtube", "")
                print(topic)
                pywhatkit.playonyt(topic)
                print("opening youtube")
                speak("opening youtube")
                print("enteing youtube automation mode")
                speak("entering youtube automation mode")
                flag = True
                while flag :
                    query = self.command()
                    YouTubeAuto(query)
                    if "exit" in query:
                        print("exiting Youtube automation mode")
                        speak("exiting Youtube automation mode")

                        break


            elif 'music' in self.query or 'song' in self.query or 'songs' in self.query : #working
                files=fnmatch.filter(os.listdir(".\music"),"*.mp3")
                d=random.choice(files)
                print("playing songs")
                os.startfile(os.path.join(".\music", d))
                

            elif "what can you do" in self.query :
                speak('''I can search wikipedia ,
                open youtube,
                search the web,
                Play music,
                send E-mails,
                chech weather,
                check news,
                search how to do anyting

                ''')


            elif "send email"  in self.query:#working
                try:
                    print("who should i send it to")
                    speak("who should i send it to")
                    to = self.command().replace("at", "@")
                    if "@" in to:
                            to = to.replace(" ", "")                                                                   
                            print(to)
                            print("what should i say")
                            speak("what should i say")
                            message = self.command()
                            print(message)
                            sendMail(to , message)
                            
                            print("do you want to save contact")
                            speak("do you want to save contact")
                            ans = self.command()
                            if "yes" in ans:
                                print("Tell me the name for contact")
                                speak("Tell me the name for contact")
                                name = self.command()
                                saveEmail(name,to)
                                print("contact saved")
                                speak("contact saved")

                            else: speak("Ok")

                    else :    
                        with open(file,'rb') as f:
                            d=pickle.load(f)
                            print (d)
                            if (d.get(to)):
                                print("what should i say")
                                speak("what should i say")
                                message = self.command()
                                print(message)
                                add = d[to]
                                add = add.replace(" ", "")   
                                sendMail(add,message) 

                            else:
                                print("contact not found , Please add contact or specify email address")
                                speak("contact not found , Please add contact or specify email address")
                                

                except smtplib.SMTPException as e:
                    print(e)
                    print("can't send email")
                    speak("can't send email")
                    

            elif "save email" in self.query or "save contact" in self.query:#working
                flag = True
                while flag:
                    print("please tell the name")
                    speak("please tell the name")
                    name=self.command()
                    print("please tell email")
                    speak("please tell email")
                    em=self.command()
                    em=em.replace("at", "@")
                    em=em.replace(" ", "")
                    print("Are you sure")    
                    speak("Are you sure")
                    choice = self.command()
                    if "no" in choice:
                        continue    
                    saveEmail(name,em)
                    break


            elif "show email" in self.query: #working
                with open(file,'rb') as f:
                    d=pickle.load(f)
                    print (d)  


            elif "weather" in self.query: 
                speak ("where to check the weather")
                print ("where to check the weather")
                city = self.command()
                weather(city)

                      
                 
            elif "how to" in self.query:
                try:
                
                    max = 1
                    how_to = search_wikihow(self.query,max)
                    assert len(how_to) ==1
                    how_to[0].print()
                    speak(how_to[0].summary)

                except exception as e:
                    print(e)
                    speak("please enter a valid request")


            elif "movies" in self.query: #working
                movies()

                    

            elif "what" in self.query:                  
                app_id = "54J27V-98XXLHRA4A"
                client = wolframalpha.Client('54J27V-98XXLHRA4A')
                res= client.query(self.query)
                ans = next(res.results).text
                print(ans)
                speak(ans)
            

            elif "search" in self.query: #working
                search = self.query.replace("search","")
                webbrowser.open_new_tab(search)
                
            
            elif "news" in self. query:#working
              news()

            
            elif "joke" in self.query: #working
                headers ={
                    'Accept': 'application/json'
                }
                res= requests.get("https://icanhazdadjoke.com/",headers=headers).json()
                joke = res["joke"]
                print(joke)
                speak(joke)

            
            elif "camera" in self.query:
                speak("press space to click and escape to exit")
                cam = cv2.VideoCapture(0)
                img_counter = 0    
                while True:
                    ret, frame = cam.read()
                    if not ret:
                        print("failed to grab Frame")
                    cv2.imshow('webcam', frame)                    
                    k=cv2.waitKey(1)
                    if k%256==27:
                        break
                    elif k%256 == 32:
                        img_name = "opencv_frame_{}.png".format(img_counter)
                        cv2.imwrite(img_name, frame)
                        img_counter+=1
                cam.release()
                cv2.destroyAllWindows()

             
            elif "alarm" in self.query:
                pass

            elif "download" in self.query and "video" in self.query:
                try:
                    print("downloading video")
                    speak("downloading video")
                    press_and_release('Ctrl + l')
                    hotkey('ctrl','c')
                    value = pyperclip.paste()
                    link = str(value)
                    url = YouTube(link)
                    print(url)
                    video = url.streams.get_highest_resolution()
                   
                    video.download()
                    print("video downloaded")
                except Exception as e:
                    print(e)

            
            elif "whatsapp" in self.query or "message" in self.query:#working
                print("what should i say")
                speak("what should i say")
                message = self.command()
                
                while flag:
                    print("please tell the number")
                    speak("please tell the number")
                    person = self.command()
                    person = str(person)
                    person = person.replace(" ","")
                    print(person)
                    print("are you sure about the number")
                    speak("are you sure about the number") 
                    choice = self.command()
                    if "yes" in choice:
                        break
                final_time = now + datetime.timedelta(minutes=2)
                hour = final_time.hour
                min = final_time.minute
                
                code = "+91"
                code = str(code)
                num = code+person
                print()
                try:
                    pywhatkit.sendwhatmsg(num, message,hour,min,90)
                except Exception as e:
                    print(e)
                

            
            elif "talk" in self.query:#working
                print("entering conversation mode")
                speak("entering conversation mode")
                chatbot = ChatBot('Eon')
                trainer= ChatterBotCorpusTrainer(chatbot, show_training_progress = False)
                trainer.train("chatterbot.corpus.english.greetings")   
                trainer.train("chatterbot.corpus.english.conversations") 
                flag = True   
                while flag:
                    sentence = self.command()
                    response = chatbot.get_response(sentence)
                    speak(response)
                    print(response)
                    if "exit" in sentence:
                        flag = False
                    else:
                        pass

            
            elif 'home screen' in self.query:

                press_and_release('windows + m')

            elif 'minimize' in self.query:

                press_and_release('windows + m')

            elif 'show start' in self.query:

                press('windows')

            elif 'open settings' in self.query:

                press_and_release('windows + i')

            elif 'open search' in self.query:

                press_and_release('windows + s')

            elif 'screen shot' in self.query:

                press_and_release('windows + SHIFT + s')

            elif 'restore windows' in  self.query:

                press_and_release('Windows + Shift + M')

                

    def command(self):
        translator = google_translator()
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration = 1)
            
            r.pause_threshold = 1
            playsound('start.mp3')
            print("Listening...")
            audio = r.listen(source)
        
        try:
            print("Recognizing...")  
            playsound('stop.mp3')  
            self.query = r.recognize_google(audio)
            print(f"User said: {self.query}")
            self.query = translator.translate(self.query,lang_tgt='en')
            self.query=self.query.lower()
            print(f"Translation : {self.query}")

        except Exception as e:
            print(e)    
            print("Say that again please...") 
            return "none"
        return self.query
        
startexecution = MainThread() 

class Main(QMainWindow) :
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.start.clicked.connect(self.StartTask)
        self.ui.stop.clicked.connect(self.close)
                                                                                            

    
    def StartTask(self):
        wish()
        self.ui.movie = QtGui.QMovie("background.gif")
        self.ui.background.setMovie(self.ui.movie)
        self.ui.movie.start()
            
        startexecution.start()   

    
app = QApplication(sys.argv)
eon = Main()
eon.setWindowTitle("Eon")
eon.setWindowIcon(QIcon("icon.jpg"))
eon.show()
status = app.exec_()
sys.exit(status)