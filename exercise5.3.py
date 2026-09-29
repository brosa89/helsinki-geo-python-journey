import pandas as pd

kumpula = pd.read_csv("data/Kumpula_temps_May_Aug_2017.csv")
rovaniemi = pd.read_csv("data/Rovaniemi_temps_May_Aug_2017.csv")

print(kumpula.head())
print("")
print(rovaniemi.head())

kumpula_median = kumpula["Celsius"].median()
rovaniemi_median = rovaniemi["Celsius"].median()

print(f"Kumpula median: {kumpula_median}")
print(f"Rovaniemi median: {rovaniemi_median}")

kumpula_may = kumpula[(kumpula["YR--MODAHRMN"] >= 201705010000) & (kumpula["YR--MODAHRMN"] < 201706010000)]
kumpula_june = kumpula[(kumpula["YR--MODAHRMN"] >= 201706010000) & (kumpula["YR--MODAHRMN"] < 201707010000)]
rovaniemi_may = rovaniemi[(rovaniemi["YR--MODAHRMN"] >= 201705010000) & (rovaniemi["YR--MODAHRMN"] < 201706010000)]
rovaniemi_june = rovaniemi[(rovaniemi["YR--MODAHRMN"] >= 201706010000) & (rovaniemi["YR--MODAHRMN"] < 201707010000)]

kumpula_may_mean = kumpula_may["Celsius"].mean()
kumpula_june_mean = kumpula_june["Celsius"].mean()
rovaniemi_may_mean = rovaniemi_may["Celsius"].mean()
rovaniemi_june_mean = rovaniemi_june["Celsius"].mean()
kumpula_may_min = kumpula_may["Celsius"].min()
kumpula_june_min = kumpula_june["Celsius"].min()
rovaniemi_may_min = rovaniemi_may["Celsius"].min()
rovaniemi_june_min = rovaniemi_june["Celsius"].min()
kumpula_may_max = kumpula_may["Celsius"].max()
kumpula_june_max = kumpula_june["Celsius"].max()
rovaniemi_may_max = rovaniemi_may["Celsius"].max()
rovaniemi_june_max = rovaniemi_june["Celsius"].max()

print(f"Kumpula mean in may: {kumpula_may_mean}")
print(f"Kumpula mean in june: {kumpula_june_mean}")
print(f"Rovaniemi mean in may: {rovaniemi_may_mean}")
print(f"Rovaniemi mean in june: {rovaniemi_june_mean}")
print(f"Kumpula min in may: {kumpula_may_min}")
print(f"Kumpula min in june: {kumpula_june_min}")
print(f"Rovaniemi min in may: {rovaniemi_may_min}")
print(f"Rovaniemi min in june: {rovaniemi_june_min}")
print(f"Kumpula max in may: {kumpula_may_max}")
print(f"Kumpula max in june: {kumpula_june_max}")
print(f"Rovaniemi max in may: {rovaniemi_may_max}")
print(f"Rovaniemi max in june: {rovaniemi_june_max}")
print(f"First values in May, Kumpula:\n{kumpula_may.head()}\n")
print(f"Last values in May, Kumpula:\n{kumpula_may.tail()}")
print(f"First values in June, Kumpula:\n{kumpula_june.head()}\n")
print(f"Last values in June, Kumpula:\n{kumpula_june.tail()}")
print(f"First values in May, Rovaniemi:\n{rovaniemi_may.head()}\n")
print(f"Last values in May, Rovaniemi:\n{rovaniemi_may.tail()}")
print(f"First values in June, Rovaniemi:\n{rovaniemi_june.head()}\n")
print(f"Last values in June, Rovaniemi:\n{rovaniemi_june.tail()}")