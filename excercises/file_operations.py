import os
import time

folder_path = input("Podaj ścieżkę katalogu: ")
filename = input("Podaj nazwę pliku: ")
file_path = folder_path + "/" + filename

os.rename(file_path, folder_path + "/" + "test.txt")