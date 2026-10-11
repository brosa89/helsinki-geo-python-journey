import pandas as pd

#reads and saves the input file into the "data" variable, with values separated by spaces, skips row 2 and converts no data values -9999 into NaN
data = pd.read_csv("data/1091402.txt", skiprows=[1], sep=r"\s+", na_values=-9999) 

#prints the first 5 and last 5 rows of the input file
print(data.head())
print(data.tail())

#metrics calculation for input file, TAVG and TMIN number of NaN, number of days, date of first and last observation, average temperature and average temperature in the summer of 1969
tavg_nodata_count = data["TAVG"].isnull().sum()
tmin_nodata_count = data["TMIN"].isnull().sum()
day_count = len(data)
first_obs = data["DATE"].iloc[0]
last_obs = data["DATE"].iloc[-1]
avg_temp = data["TAVG"].mean()
avg_temp_1969 = data[(data["DATE"]>= 19690501) & (data["DATE"] <= 19690831)]["TMAX"].mean()

print(f'Number of no-data values in column "TAVG": {tavg_nodata_count}')
print(f'Number of no-data values in column "TMIN": {tmin_nodata_count}')
print(f'Number of days: {day_count}')
print(f'Date of the first observation: {first_obs}')
print(f'Date of the last observation: {last_obs}')
print(f'Average temperature (F) for the whole dataset: {round(avg_temp, 2)}')
print(f"Average temperature (F) for the Summer of '69: {round(avg_temp_1969, 2)}")