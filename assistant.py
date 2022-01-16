import speech_recognition as sr


class Assistant:
    def __init__(self):
        self.__awake = True
        self.__listening = False
        self.__recognizer = sr.Recognizer()

    @property
    def awake(self):
        return self.__awake

    @property
    def listening(self):
        return self.__listening

    @listening.setter
    def listening(self,value: bool):
        self.__listening = value

    def listen(self):
        with sr.Microphone() as source:
            print("Je t'écoute")
            audio = self.__recognizer.listen(source)
            try:
                statement = self.__recognizer.recognize_google(audio, language='fr-FR')
                if statement is None:
                    statement = ""
                return statement.lower()
            except Exception as exception:
                print(exception)
                return "Il y a eu un problème"
