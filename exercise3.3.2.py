stations = ['Hanko Russarö', 'Heinola Asemantaus', 'Helsinki Kaisaniemi', 
            'Helsinki Malmi airfield', 'Hyvinkää Hyvinkäänkylä', 'Joutsa Savenaho', 
            'Juuka Niemelä', 'Jyväskylä airport', 'Kaarina Yltöinen', 'Kauhava airfield', 
            'Kemi Kemi-Tornio airport', 'Kotka Rankki', 'Kouvola Anjala', 
            'Kouvola Utti airport', 'Kuopio Maaninka', 'Kuusamo airport', 
            'Lieksa Lampela', 'Mustasaari Valassaaret', 'Parainen Utö', 'Pori airport', 
            'Rovaniemi Apukka', 'Salo Kärkkä', 'Savonlinna Punkaharju Laukansaari', 
            'Seinäjoki Pelmaa', 'Siikajoki Ruukki', 'Siilinjärvi Kuopio airport', 
            'Tohmajärvi Kemie', 'Utsjoki Nuorgam', 'Vaala Pelso', 'Vaasa airport', 
            'Vesanto Sonkari', 'Vieremä Kaarakkala', 'Vihti Maasoja', 'Ylitornio Meltosjärvi']

lats = [59.77, 61.2, 60.18, 60.25, 60.6, 61.88, 63.23, 62.4,
       60.39, 63.12, 65.78, 60.38, 60.7, 60.9, 63.14, 65.99,
       63.32, 63.44, 59.78, 61.47, 66.58, 60.37, 61.8, 62.94,
       64.68, 63.01, 62.24, 70.08, 64.501, 63.06, 62.92, 63.84,
       60.42, 66.53]

lons = [22.95, 26.05, 24.94, 25.05, 24.8, 26.09, 29.23, 25.67, 
       22.55, 23.04, 24.58, 26.96, 26.81, 26.95, 27.31, 29.23, 
       30.05, 21.07, 21.37, 21.79, 26.01, 23.11, 29.32, 22.49, 
       25.09, 27.8, 30.35, 27.9, 26.42, 21.75, 26.42, 27.22, 
       24.4, 24.65]

weather_stations_location = list(zip(stations, lats, lons))

print(weather_stations_location)

north_west = []
north_east = []
south_west = []
south_east = []

for station, lat, lon in weather_stations_location:
    if lat > 64.5 and lon < 26.3:
        north_west.append(station)
    elif lat < 64.5 and lon <26.3:
        south_west.append(station)
    elif lat > 64.5 and lon > 26.3:
        north_east.append(station)
    elif lat < 64.5 and lon > 26.3:
        south_east.append(station)
        
print(f"The names of the Northwest stations are:\n{north_west}")
print(f"The names of the Northeast stations are:\n{north_east}")
print(f"The names of the Southwest stations are:\n{south_west}")
print(f"The names of the Southeast stations are:\n{south_east}")
print("Total:", len(north_west) + len(north_east) + len(south_west) + len(south_east))