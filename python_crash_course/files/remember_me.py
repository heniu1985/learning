import json

FILE_PATH = "python_crash_course/files/username.json"

def get_new_username():
    """Prosi o podanie imienia i je zapisuje"""
    username = input("Podaj swoje imię: ")
    filename = FILE_PATH
    with open(filename, "w") as f:
        json.dump(username, f)
    return username

def get_stored_username():
    """Pobranie nazwy użytkownika z pliku"""
    filename = FILE_PATH
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def new_username():
    """Wywołuje funkcję get_new_username i wyświetla odpowiedni komunikat"""
    username = get_new_username()
    return f"Twoje imię zostało zapisane. {username}!"

def greet_user():
    """Przywitanie użytwkonika z wykorzystaniem jego nazwy"""
    username = get_stored_username()
    if username:
        answer = input(f"Czy to ty {username}? ")
        if answer == "y" or answer == "Y":
            print(f"Witamy ponownie, {username}!")
        else:
            new_username()
    else:
        new_username()

greet_user()