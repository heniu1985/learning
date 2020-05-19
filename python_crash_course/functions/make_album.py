def make_album(artist, title, tracks):
    """Zwraca słownik z informacją o artyście, tytule albumu i liczbie utworów"""
    album = {"Artysta": artist, "Tytuł": title, "Liczba utworów": int(tracks)}
    return album

while True:
    print("Podaj nazwę artysty, tytuł albumu i liczbę utworów na płycie:")
    print("(w celu wyświetlenia słownika i wyjścia z programu wpisz 'q' w dowolnym momencie)")

    artist = input("Artysta: ")
    if artist == "q":
        break
    title = input("Tytuł: ")
    if title == "q":
        break
    tracks = input("Liczba utworów: ")
    if tracks == "q":
        break

    slownik = make_album(artist, title, tracks)
    print(slownik)