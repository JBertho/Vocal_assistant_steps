from assistant import Assistant


def contain_wake_up_word(statement):
    return "debout alita" in statement or "debout anita" in statement


def containe_sleep_word(statement):
    return "repose-toi alita" in statement or ("repose" in statement and "alita" in statement)


def contain_dance_word(statement):
    return "danse" in statement


def find_action_to_do(statement: str, alita: Assistant):
    if contain_dance_word(statement):
        alita.start_dancing()


if __name__ == '__main__':
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
