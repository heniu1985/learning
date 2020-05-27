def file_not_found():
    """
    Wyświetla komunikat o braku pliku
    Show info about missing file
    """
    print("\nNie ma takiego pliku")

def main_path():
    """
    Śceżka do folderu z plikami
    Path to folder with files
    """
    return "python_crash_course/files/"

def file_path(filename):
    """
    Utworzenie ścieżki do pliku
    Create path to file
    """
    file_path = main_path() + filename
    return file_path

def file_read(file_path):
    """
    Wczytanie pliku
    Load file
    """
    try:
        with open(file_path) as file_object:
            content = file_object.read()
    except FileNotFoundError:
        file_not_found()
    else:
        return content

def count_words(content, filename):
    """
    Obliczanie liczby słów w podanym pliku tekstowym
    Counts number of words in a file content
    """
    try:
        content = content.split()
        num_words = len(content)
        print(f"W pliku {filename} znajduje się ok. {num_words} słów.")
    except AttributeError:
        pass

def word_number(word, content):
    """
    Obliczanie ile powtórzeń danego słowa jest w danym pliku tekstowym
    Couts how many times word is repeated in file content
    """
    number = content.lower().count(word)
    print(f"W pliku znajduje się {number} słów {word}")

def main():
    """
    Główny program
    Main programm
    """
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
                if content == None:
                    continue
                count_words(content, filename)
        if choice == "2":
                filename = input("Podaj nazwę pliku wraz z rozszerzeniem '.txt': ")
                content = file_read(file_path(filename))
                if content == None:
                    continue
                word = input("Podaj słowo, którego powtórzenia chcesz obliczyć: ")
                word_number(word, content)

main()