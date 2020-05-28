import matplotlib.pyplot as plt

FILE_PATH = "python_crash_course/project2/squares_plot.png"

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use("fivethirtyeight")
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c="Green", s=10)

# Zdefiniowanie tytułu wykresu i etykiet osi
ax.set_title("Kwadraty liczb", fontsize=25)
ax.set_xlabel("Wartość", fontsize=14)
ax.set_ylabel("Kwadraty wartości", fontsize=14)

# Zdefiniowanie wielkości etykiet
ax.tick_params(axis="both", labelsize=14)

# Zdefiniowanie zakresu dla każdej osi
ax.axis([0, 1100, 0, 1100000])

plt.ticklabel_format(useMathText=True)

# Pokazuje wykres
plt.show()

# Zapisuje wykres do pliku
plt.savefig(FILE_PATH, bbox_inches="tight")