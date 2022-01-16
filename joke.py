class Joke:

    def __init__(self, type: str, joke: str = "", setup: str = "", delivery: str = ""):
        self.__type = type
        self.__joke = joke
        self.__setup = setup
        self.__delivery = delivery

    @property
    def type(self):
        return self.__type

    @property
    def joke(self):
        return self.__joke

    @property
    def setup(self):
        return self.__setup

    @property
    def delivery(self):
        return self.__delivery
