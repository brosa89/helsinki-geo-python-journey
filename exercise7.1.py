import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

random_numbers_x = np.random.rand(1000)
random_numbers_y = np.random.rand(1000)
data = pd.DataFrame()
data["x"] = random_numbers_x
data["y"] = random_numbers_y

colors = np.random.rand(1000)

print(data.head())
assert len(data) == 1000, "There should be 1000 rows of data."
print(colors[0:10])
assert len(colors) == 1000, "There should be 1000 random numbers for colors"

data.plot.scatter(
    x="x",
    y="y",
    s=100,
    c=colors,
    colormap="rainbow",
    edgecolors="black"
)

title = "Random Points Scater Plot" 
xlabel = "x"
ylabel = "y"

plt.title(title)
plt.xlabel(xlabel)
plt.ylabel(ylabel)

outputfp = "data/scater_plot.png"
plt.savefig(outputfp)
plt.show()