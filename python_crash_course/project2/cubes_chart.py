import matplotlib.pyplot as plt

FILE_PATH = "python_crash_course/project2/cubes_plot.png"

x_values = range(1, 5001)
y_values = [x ** 3 for x in x_values]

plt.style.use("classic")
fig, ax = plt.subplots()
ax.plot(x_values, y_values, c="Green", linewidth=1)

ax.set_title("Sześciany liczb", fontsize=24)
ax.set_xlabel("Wartość", fontsize=12)
ax.set_ylabel("Sześciany wartości", fontsize=12)

ax.tick_params(axis="both", labelsize=8)

plt.ticklabel_format(useMathText=True)

plt.show()