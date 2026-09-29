import pandas as pd

kumpula = pd.read_csv("data/Kumpula_temps_May_Aug_2017.csv")
rovaniemi = pd.read_csv("data/Rovaniemi_temps_May_Aug_2017.csv")

kumpula["day"] = kumpula["YR--MODAHRMN"] // 10000
rovaniemi["day"] = rovaniemi["YR--MODAHRMN"] // 10000

kumpula_daily =  kumpula.groupby("day")["Celsius"].agg(["mean", "max", "min"])
rovaniemi_daily =  rovaniemi.groupby("day")["Celsius"].agg(["mean", "max", "min"])

print(kumpula_daily.head())
print(rovaniemi_daily.head())