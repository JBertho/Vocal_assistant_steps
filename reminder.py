from datetime import datetime


class Reminder:

    def __init__(self, hour: datetime, reason: str):
        self.__hour = hour
        self.__reason = reason

    @property
    def hour(self) -> datetime:
        return self.__hour

    @property
    def reason(self) -> str:
        return self.__reason
