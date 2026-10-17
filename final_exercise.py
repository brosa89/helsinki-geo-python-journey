import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

data = pd.read_csv("data/2315676.txt", skiprows=[1], sep=r"\s+", na_values=-9999)

data["TAVG_FILLED"] = data["TAVG"].fillna((data["TMAX"] + data["TMIN"]) / 2)

data = data.dropna(subset=["TAVG_FILLED"])

def fahr_to_celsius(temp_fahrenheit):
    """Convert temperatures from Farenheit to Celsius
    
    Parameters
    ----------
    temp_fahrenheit: numerical
        Temperature in degrees Fahrenheit.
        
    Returns
    -------
    float
        Temperature converted to degrees Celsius"""
    converted_temp = (temp_fahrenheit-32)/1.8 # converts farenheit to celsius and saves it in converted_temp
    return converted_temp # returns the variable converted_temp

data["TAVG_CELSIUS"] = fahr_to_celsius(data["TAVG_FILLED"])

data["YEAR"] = data["DATE"] // 10000
data["MONTH"] = (data["DATE"] // 100) % 100

seasons = {
    12: "Winter", 1: "Winter", 2: "Winter",
    3: "Spring", 4: "Spring", 5: "Spring",
    6: "Summer", 7: "Summer", 8: "Summer",
    9: "Autumn", 10: "Autumn", 11: "Autumn",
}
data["SEASON"] = data["MONTH"].map(seasons)

data["SEASON_YEAR"] = data["YEAR"]
data.loc[data["MONTH"] == 12, "SEASON_YEAR"] = data["YEAR"] + 1

seasonal = data.groupby(["SEASON_YEAR", "SEASON"])["TAVG_CELSIUS"].mean().reset_index()

reference_data = seasonal[(seasonal["SEASON_YEAR"] >= 1951) & (seasonal["SEASON_YEAR"] <= 1980)]
reference_temps = reference_data.groupby("SEASON")["TAVG_CELSIUS"].mean().reset_index().rename(columns={"TAVG_CELSIUS": "ref_temp"})

seasonal = seasonal.merge(reference_temps, on="SEASON")
seasonal["diff"] = seasonal["TAVG_CELSIUS"] - seasonal["ref_temp"]

print(data.head())
print("NaN on original TAVG:", data["TAVG"].isnull().sum())
print("NaN on TAVG_FILLED:", data["TAVG_FILLED"].isnull().sum())
print(data["SEASON"].nunique())
print(data[data["MONTH"] == 12].head())
print(seasonal.head(8))
print(reference_temps)
print(len(seasonal))

plot_data = seasonal[(seasonal["SEASON_YEAR"] >= 1908) & (seasonal["SEASON_YEAR"] <= 2019)]

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# winter panel (left upper corner)
winter = plot_data[plot_data["SEASON"] == "Winter"]
winter.plot(x="SEASON_YEAR", y="diff", ax=axes[0, 0])
axes[0, 0].set_title("Winter")
axes[0, 0].axhline(0, color="black", linewidth=0.5)
axes[0, 0].set_ylabel("Anomaly (°C)")

# spring panel (right upper corner)
spring = plot_data[plot_data["SEASON"] == "Spring"]
spring.plot(x="SEASON_YEAR", y="diff", ax=axes[0, 1])
axes[0, 1].set_title("Spring")
axes[0, 1].axhline(0, color="black", linewidth=0.5)
axes[0, 1].set_ylabel("Anomaly (°C)")

# summer panel (left bottom corner)
summer = plot_data[plot_data["SEASON"] == "Summer"]
summer.plot(x="SEASON_YEAR", y="diff", ax=axes[1, 0])
axes[1, 0].set_title("Summer")
axes[1, 0].axhline(0, color="black", linewidth=0.5)
axes[1, 0].set_ylabel("Anomaly (°C)")

# autumn panel (right bottom corner)
autumn = plot_data[plot_data["SEASON"] == "Autumn"]
autumn.plot(x="SEASON_YEAR", y="diff", ax=axes[1, 1])
axes[1, 1].set_title("Autumn")
axes[1, 1].axhline(0, color="black", linewidth=0.5)
axes[1, 1].set_ylabel("Anomaly (°C)")

fig.suptitle("Seasonal temperature anomalies in Sodankylä (1909–2019)")
plt.tight_layout()
plt.savefig("data/seasonal_anomalies.png")
plt.show()