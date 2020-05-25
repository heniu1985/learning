a = input("Podaj pierwszą liczbę: ")
b = input("Podaj drugą liczbę: ")

try:
    c = int(a) + int(b)
    print(c)
except ValueError:
    print("Nie można dodawać liter!!!")