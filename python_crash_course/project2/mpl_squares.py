import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use("classic")
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# Zdefiniowanie tytułu wykresu i etykiet osi
ax.set_title("Kwadraty liczb", fontsize=25)
ax.set_xlabel("Wartość", fontsize=14)
ax.set_ylabel("Kwadraty wartości", fontsize=14)

# Zdefiniowanie wielkości etykiet
ax.tick_params(axis="both", labelsize=14)

plt.show()