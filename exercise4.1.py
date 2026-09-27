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

print(f"32 degrees Fahrenheit is equal to {fahr_to_celsius(32)} degrees Celsius.")
print(f"48 degrees Fahrenheit is equal to {fahr_to_celsius(48)} degrees Celsius.")
print(f"71 degrees Fahrenheit is equal to {fahr_to_celsius(71)} degrees Celsius.")

import inspect

# Check that function exists
assert inspect.isfunction(fahr_to_celsius), 'Fahr_to_celsius should be a function.'

# Check that the function has a single parameter and the parameter name is correct
params = list(inspect.signature(fahr_to_celsius).parameters.keys())
assert len(params) == 1, 'The function should have one parameter'
assert params[0] == 'temp_fahrenheit', 'The parameter name should be "temp_fahrenheit".'

# Check that the function produces correct answers for:
# 1. What is 48° Fahrenheit in Celsius? 
assert round(fahr_to_celsius(48), 2) == 8.89

# 2. What about 71° Fahrenheit in Celsius?
assert round(fahr_to_celsius(71), 2) == 21.67