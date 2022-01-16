from dotenv import load_dotenv

from assistant import Assistant
from music import Music


def contain_wake_up_word(statement):
    return "debout alita" in statement or "debout anita" in statement or "debout à l'état" in statement


def containe_sleep_word(statement):
    return "repose-toi alita" in statement or ("repose" in statement and "alita" in statement)


def contain_dance_word(statement):
    return "danse" in statement


def contain_weather_word(statement):
    return "météo" in statement or "temps" in statement


def contain_start_music_word(statement):
    return "lance" in statement and "musique" in statement


def contain_stop_music_word(statement):
    return "stop" in statement and "musique" in statement


def contain_joke_word(statement):
    return "blague" in statement or "rire" in statement


def find_action_to_do(statement: str, alita: Assistant):
    if contain_dance_word(statement):
        alita.start_dancing()
    elif contain_weather_word(statement):
        alita.tell_weather()
    elif contain_joke_word(statement):
        alita.tell_joke()
    elif contain_start_music_word(statement):
        music_started = Music.play_song()
        if music_started:
            print("C'est parti !")
        else:
            print("Je n'ai pas pu lancer le son")
    elif contain_stop_music_word(statement):
        music_stoped = Music.stop_song()
        if music_stoped:
            print("J'ai stoppé la musique")
        else:
            print("Il n'y avait pas de musique")


if __name__ == '__main__':
    load_dotenv()
    print("hello Alita")

    alita = Assistant()

    while alita.awake:
        statement = alita.listen()
        print(statement)

        if contain_wake_up_word(statement):
            alita.listening = True
            print("Avez-vous besoin de moi ?")

        elif containe_sleep_word(statement) and alita.listening:
            alita.listening = False
            print("A la prochaine")

        elif alita.listening:
            find_action_to_do(statement, alita)
