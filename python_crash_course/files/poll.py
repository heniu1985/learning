filename = "python_crash_course/files/answers.txt"

while True:
    print("W celu zakończenia ankiety wciśnik klawisz 'q'")
    answer = input("Dlaczego lubisz programowanie? ")
    if answer == "q":
        break
    else:
        with open(filename, "a") as file_object:
            file_object.write(answer + "\n")
