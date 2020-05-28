import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Tworzenie nowego błądzenia losowego, dopóki program pozostanie aktywny.
while True:
    # Przygotowanie danych błądzenia losowego i wyświetlenie punktów.
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # Wyświetlenie punktów błądzenie losowego.
    plt.style.use("classic")
    fig, ax = plt.subplots(figsize=(16, 9), dpi=128)
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor="none", s=1)

    # Podkreślenie pierwszego i ostatniego punktu błądzenia losowego.
    ax.scatter(0, 0, c="green", edgecolor="none", s=25)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolor="none", s=15)

    # Ukrycie osi.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()
    
    keep_running = input("Utworzyć kolejne błądzenie losowe? (t/n): ")
    if keep_running == "n":
        break