from assistant import Assistant


def contain_wake_up_word(statement):
    return "debout alita" in statement or "debout anita" in statement


def containe_sleep_word(statement):
    return "repose-toi alita" in statement or ("repose" in statement and "alita" in statement)


if __name__ == '__main__':
    print("hello Alita")

    alita = Assistant()

    while alita.awake:
        statement = alita.listen()
        print(statement)

        if contain_wake_up_word(statement):
            alita.listening = True
            print("Avez-vous besoin de moi ?")
            
        if containe_sleep_word(statement) and alita.listening:
            alita.listening = False
            print("A la prochaine")
        


