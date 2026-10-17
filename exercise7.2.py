import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import os
import hvplot.pandas

fp = "data/helsinki-vantaa.csv"

data = pd.read_csv(
    fp,
    parse_dates=["DATE"],
    index_col="DATE",
)

data = data.sort_index()
selection = data.loc["1988":"2018"]

print(data.head())
print(len(data))
print(data.tail())
print(selection.head())
print(selection.tail())
print(f'Number of rows: {len(selection)}')

line_plot = selection["TEMP_C"].plot(
    figsize=(14,6),
    color="k",
    linestyle="-",
    marker="o"
)

plt.title("Helsinki-Vantaa Airport")
plt.xlabel("Time")
plt.ylabel("Temperature (Celsius)")

outputfp = "data/temp_line_plot.png"
plt.savefig(outputfp)
plt.show()
os.path.exists(outputfp)

plot = selection["TEMP_C"].hvplot(
    title="Helsinki-Vantaa Airport",
    xlabel="Time",
    ylabel="Temperature (Celsius)"
)

hvplot.save(plot, "data/temp_interactive.html")
hvplot.show(plot)