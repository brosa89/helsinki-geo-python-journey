"""Functions for temperature conversion and classification"""

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

def temp_classifier(temp_celsius: float) -> int: # classifies temperature into 4 classes
    """Classifies temperatures in Celsius into a scale
    Parameters
    ----------
    temp_celsius: numerical
        Temperature in degrees Celsius.
            
    Returns
    -------
    int
        Class from 0 to 3."""
    if temp_celsius < -2:
        return 0
    elif temp_celsius < 2:
        return 1
    elif temp_celsius < 15:
        return 2
    else:
        return 3