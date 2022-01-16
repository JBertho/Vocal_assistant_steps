from assistant import Assistant


def contain_wake_up_word(statement):
    return "debout alita" in statement


def contain_sleep_word(statement):
    return "repose-toi alita" in statement


if __name__ == '__main__':
    print("hello Alita")

    alita = Assistant()

    while alita.awake:
        print("Je suis toujours la")
        statement = alita.listen()
        print(statement)

        if contain_wake_up_word(statement):
            alita.listening = True
            print("Je vous écoute")

        if contain_sleep_word(statement):
            alita.listening = False
            print("Je retourne au repos")

