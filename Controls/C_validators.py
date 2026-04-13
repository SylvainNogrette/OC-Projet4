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
                print("Vous devez saisir le nom du joueur.")
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
                print("Vous devez saisir le prénom du joueur.")
                return wrapper()
        except Exception:
            print(Exception)
            return wrapper()
    return wrapper


def check_if_no_duplicate_player(input_playerID):
    def wrapper():
        input = input_playerID()
        if id_is_in_db(input, "player"):
            print(
                "Un joueur possède déjà cet identifiant."
                "Vérifiez votre saisie")
            return wrapper()
        else:
            return input
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
