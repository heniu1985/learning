import json

FILE_PATH = "python_crash_course/files/favorite_number.json"

def save_favorite_number():
    """Zapisuje ulubioną liczbę"""
    favorite_number = input("Podaj ulubioną liczbę: ")
    filename = FILE_PATH
    with open(filename, "w") as file_object:
        json.dump(favorite_number, file_object)
    return favorite_number

def get_favorite_number():
    """Wyświetla ulubioną liczbę"""
    filename = FILE_PATH
    try:
        with open(filename) as file_object:
            favorite_number = json.load(file_object)
    except FileNotFoundError:
        return False
    else:
        return favorite_number

def main():
    """Główny kod programu"""
    favorite_number = get_favorite_number()
    if favorite_number:
        print(f"Twoja ulubiona liczba to {favorite_number}")
    else:
        favorite_number = save_favorite_number()
        print(f"Twój ulubiony numer został zapisany i jest następujący {favorite_number}")

main()