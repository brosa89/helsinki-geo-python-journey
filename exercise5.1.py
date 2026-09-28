import pandas as pd

#reads the .csv file and stores in the "data" variable
data = pd.read_csv("data/6153237444115dat.csv", na_values=['*','**','***','****','*****','******'])

print(data.head())

row_count = len(data)
column_names = data.columns.values
column_datatypes = data.dtypes
temp_mean = data["TEMP"].mean()
temp_max_std = data["MAX"].std()
station_count = data["USAF"].nunique()

# Check number of rows
print(f"There are {row_count} rows")
# Check the name of the columns
print(f"The columns are: \n{column_names}")
# Check the columns data types
print(f"The column types are: \n{column_datatypes}")
# Check mean temperature value
print(f"The mean temperature in Fahrenheit is {round(temp_mean,1)}")
# Check standard deviation value
print(f"The standard deviation of maximum temperature is {round(temp_max_std, 1)}")
# Check number of stations value
print(f"The number of unique stations is {station_count}")