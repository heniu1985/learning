filename = "/home/heniu/Programowanie/Nauka/Python/learning/python_crash_course/files/guest_book.txt"

print("W celu zakończenia dodawania gości wciśnij klawisz 'q'")
while True:
    guest = input("Proszę podać imię: ")
    
    if guest == "q":
        break
    else:
        print(f"Witaj {guest.title()}")
        with open(filename, "a") as file_object:
            file_object.write(guest + "\n")
