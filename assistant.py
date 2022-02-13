from datetime import datetime

import speech_recognition as sr
import time

from joker import Joker
from music import Music
from synthesizer import Synthesizer
from weather import Weather
from reminder import Reminder


class Assistant:
    def __init__(self):
        self.__awake = True
        self.__listening = False
        self.__recognizer = sr.Recognizer()
        self.__weather = Weather()
        self.__joker = Joker()
        self.__reminders: [Reminder] = []
        self.__last_action_time = datetime.now()
        self.__synthesizer = Synthesizer()

    @property
    def last_action_time(self):
        return self.__last_action_time

    @last_action_time.setter
    def last_action_time(self, value):
        self.__last_action_time = value

    @property
    def awake(self):
        return self.__awake

    @awake.setter
    def awake(self,value):
        self.__awake = value

    @property
    def listening(self):
        return self.__listening

    @listening.setter
    def listening(self, value: bool):
        self.__listening = value

    def listen(self):
        with sr.Microphone() as source:

            if Music.is_playing():
                self.__recognizer.energy_threshold = 2000
            else:
                self.__recognizer.energy_threshold = 300
            print("Je t'écoute")
            try:
                audio = self.__recognizer.listen(source, timeout=4,phrase_time_limit=4)
                statement = self.__recognizer.recognize_google(audio, language='fr-FR')
                if statement is None:
                    statement = ""
                return statement.lower()
            except (sr.WaitTimeoutError, sr.UnknownValueError) as _:
                return ""

    def start_dancing(self):
        for i in range(10):
            print("♪┏( ・o･)┛♪┗ ( ･o･) ┓♪\n")
            time.sleep(1)
            print("♪┗ (・o･ )┓♪┏ (･o･ ) ┛♪\n")
            time.sleep(1)

    def tell_weather(self):
        self.__synthesizer.talk("De quelle ville veux-tu la météo ?")
        city = self.listen()
        city_weather = self.__weather.get_city_weather(city)
        self.__synthesizer.talk(city_weather)

    def tell_joke(self):
        joke = self.__joker.get_joke()
        if joke.type == "single":
            self.__synthesizer.talk(joke.joke)
        else:
            self.__synthesizer.talk(joke.setup)
            time.sleep(1)
            self.__synthesizer.talk(joke.delivery)

    def add_reminder(self):
        self.__synthesizer.talk("Pour quelle heure est-ce tu veux ce rappel ?")
        hour = self.listen()
        self.__synthesizer.talk("Pour quelle motif veux-tu ce rappel ?")
        reason = self.listen()
        hour_in_datetime = datetime.strptime(hour, "%Hh%M")
        reminder = Reminder(hour_in_datetime, reason)
        self.__reminders.append(reminder)
        self.__synthesizer.talk(f"OK ! Rappel programmé à {reminder.hour.time()} pour {reminder.reason}")

    def check_reminders(self):
        hour = datetime.now().time()
        for index, reminder in enumerate(self.__reminders):
            if reminder.hour.time() <= hour:
                self.__synthesizer.talk(f"RAPPEL : {reminder.reason}")
                self.__reminders.pop(index)

    def talk(self, output):
        self.__synthesizer.talk(output)
