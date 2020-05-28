from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

FILE_PATH = "python_crash_course/project2/d6.html"
# Utworzenie kości do gry
die = Die()

# Wykonanie pewnej liczby rzutów i umieszczenie wyników na liście.
results = []
for roll_num in range(1_000):
    result = die.roll()
    results.append(result)

# Analiza wyników.
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Wizualizacja wyników.
x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {"title": "Wynik"}
y_axis_config = {"title": "Częstotliwość występowania wartorści"}
my_layout = Layout(title="Wynik rzucania pojedynczą kością D6 tysiąc razy", xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({"data": data, "layout": my_layout}, filename=FILE_PATH)