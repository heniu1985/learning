cats_path = "python_crash_course/exceptions/cats.txt"
dogs_path = "python_crash_course/exceptions/dogs.txt"

try:
    with open(cats_path) as file_object:
        cats = file_object.read()
    print("Koty:")
    print(cats)
except FileNotFoundError:
    pass

try:
    with open(dogs_path) as file_object:
        dogs = file_object.read()
    print("\nPsy:")
    print(dogs)
except FileNotFoundError:
    pass
