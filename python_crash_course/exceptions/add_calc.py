print("Witamy w kalkulatorze dodawania!")

while True:
    a = input("Podaj pierwszą liczbę lub wpisz 'exit': ")

    if a == "exit":
        break
    
    b = input("Podaj drugą liczbę lub wpisz 'exit': ")
    if b == "exit":
        break
    else:
        try:
            print(f"Suma wynosi: {int(a) + int(b)}")
        except ValueError:
            print("Nie można dodawać liter!!!")
