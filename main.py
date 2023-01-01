import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import googlesearch
import pyjokes
from selenium import webdriver


listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
rate = engine.getProperty('rate')   # getting details of current speaking rate
engine.setProperty('rate', 125)     # setting up new voice rate

engine.say("Hi Joy!")
print("Hi Joy! I am here for you now!")
engine.say('I am your Cat')
engine.say('What I can do for you?')
engine.runAndWait()

def talk(text):
    engine.say(text)
    # engine.say('What I can do for you?')
    engine.runAndWait()

def take_commands():
    try:
        with sr.Microphone() as source:
            print('listening........')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'cat' in command:
                command = command.replace('cat', '')
            # talk(command)
            # print(command)

    except:
        pass

    return command

def run_cat():
    command = take_commands()
    if 'play' in command:
        song = command.replace('play', ' ')
        talk('Playing' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M %p')
        print(time)
        talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', ' ')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)

    elif 'tell me something about' in command:
        person = command.replace('who the heck is', ' ')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)

    elif 'search' in command:
        G_search = command.replace('search', ' ')
        browser = webdriver.Chrome('chromedriver.exe')
        elements = browser.get("http://www.google.com/search?q="+ G_search + "&start")
        # info = googlesearch.search(command, tld="co.in", num=10, stop=10, pause=2)
        print(elements)
        talk(elements)

    elif 'what' in command:
        browser = webdriver.Chrome('chromedriver.exe')
        elements = browser.get("http://www.google.com/search?q="+ command + "&start")
        # info = googlesearch.search(command, tld="co.in", num=10, stop=10, pause=2)
        print(elements)
        talk(elements)

    elif 'google' in command:
        G_search = command.replace('google', ' ')
        browser = webdriver.Chrome('chromedriver.exe')
        elements = browser.get("http://www.google.com/search?q="+ G_search + "&start")
        # info = googlesearch.search(command, tld="co.in", num=10, stop=10, pause=2)
        print(elements)
        talk(elements)

    elif 'joke' in command:
        joke = pyjokes.get_joke()
        print(joke)
        talk(joke)
    elif 'bit' in command:
        joke = pyjokes.get_joke()
        print('What do you call eight hobbits? A hobbyte?')
        talk('What do you call eight hobbits? A hobbyte?')

    elif 'are you single' in command:
        browser = webdriver.Chrome('chromedriver.exe')
        elements = browser.get("https://www.instagram.com/p/CmheC7VLum0/")
        print("Do you know her?")
        talk("Do you know her?")
        print("Because I do and I can contact her hahhahahaha")
        talk("Because I do and I can contact her hahhahahaha")

    elif 'goodbye' in command:
        print('See you Soon Joy !')
        talk("Will miss you baby")
        talk('bye bye')
        quit()
    else:
        talk('Please say the command again.')
    print(command)

while True:
    run_cat()