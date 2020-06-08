import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

FILE_PATH = "python_crash_course/project2/data/eq_data_1_day_m1.json"

# Analiza struktury danych
filename = FILE_PATH
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data["features"]

mags, lons, lats, hover_texts = [], [], [], []
for eq_dict in all_eq_dicts:
    mags.append(eq_dict["properties"]["mag"])
    lons.append(eq_dict["geometry"]["coordinates"][0])
    lats.append(eq_dict["geometry"]["coordinates"][1])
    hover_texts.append(eq_dict["properties"]["title"])

# Mapa trzęsień ziemi.
data = [{
    "type": "scattergeo",
    "lon": lons,
    "lat": lats,
    "text": hover_texts,
    "marker": {
        "size": [5*mag for mag in mags],
        "color": mags,
        "colorscale": "Greens",
        "reversescale": False,
        "colorbar": {"title": "Siła"},
    },
}]

title = all_eq_data["metadata"]["title"]
my_layout = Layout(title=title)

fig = {"data": data, "layout": my_layout}
offline.plot(fig, filename="python_crash_course/project2/global_earthquakes.html")