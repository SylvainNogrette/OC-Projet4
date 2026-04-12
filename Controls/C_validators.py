from datetime import datetime
import re


from Models.M_DB_manager import id_is_in_db


def validate_name(input_name):
    def wrapper():
        try:
            input = input_name()
            if input != "":
                return input
            else:
                print("Vous devez saisir le name du joueur.")
                return wrapper()
        except Exception:
            print(Exception)
            return wrapper()
    return wrapper


def validate_firstname(input_firstname):
    def wrapper():
        try:
            input = input_firstname()
            if input != "":
                return input
            else:
                print("Vous devez saisir le firstname du joueur.")
                return wrapper()
        except Exception:
            print(Exception)
            return wrapper()
    return wrapper


def validate_player_ID(input_playerID):
    def wrapper():
        try:
            input = input_playerID()
            patternIsOk = re.match(r"[A-Z]{2}\d{5}", input)
            if patternIsOk:
                return input
            else:
                print("L'identifiant saisie n'a pas la bonne syntaxe,"
                      "réessayer")
                return wrapper()
        except Exception:
            print(Exception)
            return wrapper()
    return wrapper


def validate_date(input_date):
    def wrapper():
        try:
            input = input_date()
            result = datetime.strptime(input, "%d/%m/%Y")
            resultstring = result.strftime("%m/%d/%Y")
            return resultstring
        except Exception:
            print("Le format JJ/MM/AAAA n'est pas respecté.")
            return wrapper()
    return wrapper


def validate_date_plus_hour(input_date_plus_hour):
    def wrapper():
        try:
            input = input_date_plus_hour()
            result = datetime.strptime(input, "%d/%m/%Y, %H:%M")
            result_string = result.strftime("%d/%m/%Y, %H:%M")
            return result_string
        except Exception:
            print("Le format JJ/MM/AAAA, hh:mm n'est pas respecté")
            return wrapper()
    return wrapper


def check_if_no_duplicate_player(id_player):
    if id_is_in_db(id_player, "player"):
        print(
            '''Un joueur possède déjà cet identifiant. Vérifiez votre saisie
            ou corriger l'identifiant du joueur déjà dans la base.''')
        return
    return True


def check_if_date_follow_each_other(date1: str, date2: str):
    firstdate = datetime.strptime(date1, "%d/%m/%Y, %H:%M")
    seconddate = datetime.strptime(date2, "%d/%m/%Y, %H:%M")
    return firstdate < seconddate


def validate_dates_are_chronologic(input, anterior_date):
    def wrapper():
        try:
            date_input = input()
            check_if_date_follow_each_other(anterior_date, date_input)
        except Exception:
            print(f"La date saisie ne peut être avant {date_input}.")
            return wrapper()
    return wrapper
