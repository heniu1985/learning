import csv
from datetime import datetime

import matplotlib.pyplot as plt

DATA_FILE_PATH = "python_crash_course/project2/data/sitka_weather_2018_simple.csv"

filename = DATA_FILE_PATH
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Pobieranie temeratur maksymalnych z pliku.
    dates, highs = [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)

# Dane wykresu.
plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.plot(dates, highs, c="red")

# Formatowanie wykresu
ax.set_title("Najwyższa temeratura dnia - 2018", fontsize=24)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylabel("Temperatura (F)", fontsize=16)
ax.tick_params(axis="both", which="major", labelsize=16)

plt.show()