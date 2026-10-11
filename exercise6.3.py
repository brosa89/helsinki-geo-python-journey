import pandas as pd

#reads and saves the input file into the "data" variable, with values separated by spaces, skips row 2 and converts no data values -9999 into NaN
data = pd.read_csv("data/1091402.txt", skiprows=[1], sep=r"\s+", na_values=-9999)

#convert data in "DATE" column into only year and month
data["year_month"] = data["DATE"] // 100

#group data by year and month
monthly_data = data.groupby("year_month").mean(numeric_only=True)

#convert temperature in "TAVG" into celsius
monthly_data["temp_celsius"] = (monthly_data["TAVG"] - 32) / 1.8

monthly_data["month"] = monthly_data.index % 100
monthly_data["year"] = monthly_data.index // 100

reference_data = monthly_data[(monthly_data["year"] >= 1952) & (monthly_data["year"] <= 1980)]
reference_temps = reference_data.groupby("month")["temp_celsius"].mean().reset_index().rename(columns={"temp_celsius": "ref_temp"})

monthly_data = monthly_data.merge(reference_temps, on="month")
monthly_data["diff"] = monthly_data["temp_celsius"] - monthly_data["ref_temp"]

print(monthly_data.head())
print(reference_temps)
print(monthly_data[["temp_celsius", "ref_temp", "diff"]].describe())

#month with the highest positive anomaly
pos = monthly_data.loc[monthly_data["diff"].idxmax()]
print(f"The highest positive anomaly is {pos['diff']:.2f} ºC in year {int(pos['year'])} month {int(pos['month'])}")

#month with the highest negative anomaly
neg = monthly_data.loc[monthly_data["diff"].idxmin()]
print(f"The highest negative anomaly is {neg['diff']:.2f} ºC in year {int(neg['year'])} month {int(neg['month'])}")

#month with the highest absolute anomaly
absolute = monthly_data.loc[monthly_data["diff"].abs().idxmax()]
print(f"The largest absolute anomaly is {absolute['diff']:.2f} ºC in year {int(absolute['year'])} month {int(absolute['month'])}")
