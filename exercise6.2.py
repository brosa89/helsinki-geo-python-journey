import pandas as pd

#reads and saves the input file into the "data" variable, with values separated by spaces, skips row 2 and converts no data values -9999 into NaN
data = pd.read_csv("data/1091402.txt", skiprows=[1], sep=r"\s+", na_values=-9999)

#convert data in "DATE" column into only year and month
data["year_month"] = data["DATE"] // 100

#group data by year and month
monthly_data = data.groupby("year_month").mean(numeric_only=True)

#convert temperature in "TAVG" into celsius
monthly_data["temp_celsius"] = (monthly_data["TAVG"] - 32) / 1.8

print(data.head())
print(monthly_data.head())
print(len(monthly_data))
print(monthly_data.columns.values)
print(monthly_data["temp_celsius"].mean())
print(round(monthly_data["temp_celsius"].median(), 2))