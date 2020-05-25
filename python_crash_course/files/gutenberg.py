def file_not_found():
    print("\nNie ma takiego pliku")

def main_path():
    """Śceżka do folderu z plikami"""
    return "python_crash_course/files/"

def file_path(filename):
    """Utworzenie ścieżki do pliku"""
    file_path = main_path() + filename
    return file_path

def file_read(file_path):
    """Wczytanie pliku"""
    try:
        with open(file_path) as file_object:
            content = file_object.read()
    except FileNotFoundError:
        file_not_found()
    else:
        return content

def count_words(content, filename):
    """Obliczanie liczby słów w podanym pliku tekstowym"""
    try:
        content = content.split()
        num_words = len(content)
        print(f"W pliku {filename} znajduje się ok. {num_words} słów.")
    except AttributeError:
        pass

def word_number(word, content):
    """Obliczanie ile powtórzeń danego słowa jest w danym pliku tekstowym"""
    number = content.lower().count(word)
    print(f"W pliku znajdujes się {number} słów {word}")

def action():
    """Główny program"""
    print("Witaj!")
    while True:
        print("\nWciśnij 1 aby obliczyć ile jest słów w danym pliku.")
        print("Wciśnij 2 aby obliczyć ile razy dane słowo pojawia się w danym pliku.")
        print("Wciśnij q aby zakończyć.\n")
        choice = input()
        if choice == "q":
            break
        if choice == "1":
                filename = input("Podaj nazwę pliku wraz z rozszerzeniem '.txt': ")
                content = file_read(file_path(filename))
                count_words(content, filename)
        if choice == "2":
                filename = input("Podaj nazwę pliku wraz z rozszerzeniem '.txt': ")
                content = file_read(file_path(filename))
                word = input("Podaj słowo, którego powtórzenia chcesz obliczyć: ")
                word_number(word, content)
        if choice != "1" or choice != "2":
            continue

action()