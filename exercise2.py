station_names =["lighthouse", "Harmaja", "Suomelina aaltopujo", "Kumpula", "Kaisainiemi"]
station_start_years = [2003, 1989, 2016, 2005, 1844]

assert len(station_names) == 5, 'The station_names list should have 5 items'
assert len(station_start_years) == 5, 'The station_start_years list should have 5 items.'
assert station_names[0] == 'lighthouse', 'The fisrt item in the station_names list should be "lighthouse".'
assert station_start_years[0] == 2003, 'The first item in the station_start_years list should be 2003.'

station_names.append("Malmi Airfield") 
station_names.append("Vuosaari harbour")
station_names.append("Kaivopuisto") 

station_start_years.append(1937) 
station_start_years.append(2012)
station_start_years.append(1904)

assert len(station_names) == 8, 'The station_names list should have 8 items.'
assert len(station_start_years) == 8, 'The station_start_years list should have 8 items.'
assert station_names[-1] == "Kaivopuisto", 'The station_names list last item should be "Kaivopuisto".'
assert station_start_years[-1] == 1904, 'The station_start_years list last item should be 1904.'

station_names.sort()
station_start_years.sort(reverse=True)

assert station_names[0] == 'Harmaja', 'The first item in stations_names list should be "Harmaja".'
assert station_start_years[0] == 2016, 'The first item in station_start_year list should be 2016.'

# The sorting methods used will not result as the stations would be in a diferent order then their corresponding starting year. The best way should be first use the comand zip(station_names, stations_start_year) and then sort.