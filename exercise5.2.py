import pandas as pd

# Reads and stores the .csv file in the 'data' variable 
data = pd.read_csv("data/6153237444115dat.csv", na_values=['*','**','***','****','*****','******'])

print(data.head())

row_count = len(data)
print(f"There are {row_count} rows in data.")

# Selects the relevant columns and stores them into the 'selected' variable
selected = data.loc[:, ["USAF", "YR--MODAHRMN", "TEMP", "MAX", "MIN"]].dropna(subset=["TEMP"]).copy()

print(selected.head())
print(f"There are {len(selected)} rows in selected.")

# Defines a function ro convert fahrneheit to celsius
def fahr_to_celsius(temp_fahrenheit):
    """Convert temperatures from Fahrenheit to Celsius
    
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

# Converts the 'TEMP' values to celsisus and stores them in 'Celsius'
selected["Celsius"] = fahr_to_celsius(selected["TEMP"])
selected["Celsius"] = selected["Celsius"].round(0).astype(int)

print(selected.head())
print(selected.dtypes)

# Separates the data into two DataFrames with the Kumpula and Rovaniemi stations
kumpula = selected[selected["USAF"] == 29980]
rovaniemi = selected[selected["USAF"] == 28450]

print(f"Kumpula: \n{kumpula.head()}\n")
print(f"Rovaniemi: \n{rovaniemi.head()}\n")
print(f"Kumpula: {len(kumpula)}, Rovaniemi: {len(rovaniemi)}, sum: {len(kumpula)+len(rovaniemi)}")

# Saves the two new DataFrames into two separate .csv files
output_kumpula = "data/Kumpula_temps_May_Aug_2017.csv"
output_rovaniemi = "data/Rovaniemi_temps_May_Aug_2017.csv"

kumpula.to_csv(output_kumpula, sep=",", index=False, float_format="%.2f")
rovaniemi.to_csv(output_rovaniemi, sep=",", index=False, float_format="%.2f")