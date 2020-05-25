guest = input("Proszę podać imię: ")

filename = "/home/heniu/Programowanie/Nauka/Python/learning/python_crash_course/files/guest.txt"

with open(filename, "w") as file_object:
    file_object.write(guest)