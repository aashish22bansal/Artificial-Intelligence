#!/usr/bin/env python
# coding: utf-8

# # Attempt 1

# In[15]:


#pip install SpeechRecognition
#pip install gtts

import speech_recognition as sr
import webbrowser as wb
import requests
import pyttsx
import speak
from bs4 import BeautifulSoup

#pyttsx3.init()

chrome_path='C:/Program File (x86)/Google/Chrome/Application'

def Print_on_screen():
    r = sr.Recognizer()
    with get_pyaudio() as source: #sr.Microphone()
        print("Please say something!")
        audio=r.listen(source)
    try:
        print("According to Google, this is what you just said:- "+r.recognize_google(audio))
    except:
        pass


def Search_URL_in_Browser():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Please say something!")
        audio=r.listen(source)
        print("Done")
    try:
        text=r.recognize_google(audio)
        print("According to Google, this is what you just said:- "+r.recognize_google(audio))
        wb.gwt(chrome_path).open(text)
    except Exception as e:
        print(e)

def tts(text,lang):
    file=gTTS(text=text,lang=lang)
    filename='/temp/temp.mp3'
    file.save(filename)
    
    music=pyglet.media.load(filename,streaming=False)
    music.play()
    
    time.sleep(music.duration)
    os.remove(filename)

def Search_in_Browser():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Please say something!")
        audio=r.listen(source)
        print("Done")
    try:
        text=r.recognize_google(audio)
        print("According to Google, this is what you just said:- "+text)
        lang-'en'
        
        speak.tts(text,lang)
        
        f_text='https://www.google.co.in/search?q='+text
        wb.gwt(chrome_path).open(text)
    except Exception as e:
        print(e)

def Input_Online_Search():
    '''r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Say Something!")
        audio=r.listen(source)
        print("Done!")
    #text=r.recognize_google(audio)'''
    search_item=input("Enter what do you want to search: ") # Enter the query
    URL="https://www.google.co.in/search?q="+search_item
    response=requests.get(URL)
    soup=BeautifulSoup(response.text,"lxml")
    for item in soup.select(".r a"):
        print(item.text)
        speak.tts(item.text,'en')
        break
    print("This is the first website which you will find when you will search it up online.\n Completed.")


def main():
    print("Welcome to the Model for converting Text-to-Speech")
    print("Here is a list of all the things which I can do:")
    print("\n1. Convert Voice to a Text Message and print it on screen")
    print("\n2. Take some URL and search it up on Google")
    print("\n3. Search for something online")
    print("\n4. Enter something to search online")
    option=int(input('\nEnter your choice: '))
    if option==1:
        Print_on_screen()
    elif option==2:
        Search_URL_in_Browser()
    elif option==3:
        Input_Online_Search()
    elif option==4:
        Input_Online_Search()
    print('THE END')
        
if __name__=='__main__':
    main()


# # Attempt 2

# In[ ]:


#pip install SpeechRecognition
#pip install gtts

import speech_recognition as sr
import webbrowser as wb
import requests
import time
#import speak
from bs4 import BeautifulSoup

chrome_path=('C:/Program File (x86)/Google/Chrome/Application')

def Print_on_screen():
    r = sr.Recognizer()
    with get_pyaudio() as source: #sr.Microphone()
        print("Please say something!")
        audio=r.listen(source)
    try:
        print("According to Google, this is what you just said:- "+r.recognize_google(audio))
    except:
        pass
    return (Print_on_screen())

def Search_URL_in_Browser():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Please say something!")
        audio=r.listen(source)
        print("Done")
    try:
        text=r.recognize_google(audio)
        print("According to Google, this is what you just said:- "+r.recognize_google(audio))
        wb.gwt(chrome_path).open(text)
    except Exception as e:
        print(e)
    return (Search_URL_in_Browser())

def tts(text,lang):
    file=gtts(text=text,lang=lang)
    filename='/temp/temp.mp3'
    file.save(filename)
    
    music=pyglet.media.load(filename,streaming=False)
    music.play()
    
    time.sleep(music.duration)
    os.remove(filename)
    return (tts())

def Search_in_Browser():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Please say something!")
        audio=r.listen(source)
        print("Done")
    try:
        text=r.recognize_google(audio)
        print("According to Google, this is what you just said:- "+text)
        lang-'en'
        
        speak.tts(text,lang)
        
        f_text='https://www.google.co.in/search?q='+text
        wb.gwt(chrome_path).open(text)
    except Exception as e:
        print(e)
    return (Search_in_Browser())

def Input_Online_Search():
    '''r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Say Something!")
        audio=r.listen(source)
        print("Done!")
    #text=r.recognize_google(audio)'''
    search_item=input("Enter what do you want to search: ") # Enter the query
    URL="https://www.google.co.in/search?q="+search_item
    response=requests.get(URL)
    soup=BeautifulSoup(response.text,"lxml")
    for item in soup.select(".r a"):
        print(item.text)
        speak.tts(item.text,'en')
        break
    print("This is the first website which you will find when you will search it up online.\n Completed.")
    return (Input_Online_Search())

def main():
    ans='y'
    while ans=='Y' or ans=='y':
        print("Welcome to the Model for converting Text-to-Speech")
        print("Here is a list of all the things which I can do:")
        print("1. Convert Voice to a Text Message and print it on screen")
        print("2. Take some URL and search it up on Google")
        print("3. Search for something online")
        print("4. Enter something to search online")
        option=int(input('\nEnter your choice: '))
        if option==1:
            Print_on_screen()
        elif option==2:
            Search_URL_in_Browser()
        elif option==3:
            Input_Online_Search()
        elif option--4:
            Input_Online_Search()
        ans=input('Do you want to run it again?[Y/N]: ')
    print('THE END')
    return (main())


# In[ ]:




