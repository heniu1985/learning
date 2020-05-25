file_path = "python_crash_course/files/learning_python.txt"

# Odczyt całego pliku
print("\nPrzykład pierwszy")

with open(file_path) as file_object:
    content = file_object.read()
print(content)

# Odczyt przez iterację pętlą for
print("\nPrzykład drugi")

with open(file_path) as file_object:
    for line in file_object:
        print(line.strip())

# Odczyt pliku przez umieszczenie wierszy na liście
print("\nPrzykład trzeci")

with open(file_path) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.strip())

# Zmiana słowa
print("\nZmiana słowa Python na C")

with open(file_path) as file_object:
    lines = file_object.readlines()

for line in lines:
    line = line.replace("Pythonie", "C")
    print(line.rstrip())