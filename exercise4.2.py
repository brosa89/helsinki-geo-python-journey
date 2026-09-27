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
    
print(f"The class value for 16.5 degrees Celsius is {temp_classifier(16.5)}.")
print(f"The class value for 2 degrees Celsius is {temp_classifier(2)}.")
    
import inspect

# Check that function exists
assert inspect.isfunction(temp_classifier)
# Check that the function has a single parameter and the pamameter name is correct
params = list(inspect.signature(temp_classifier).parameters.keys())
assert len(params) == 1
assert params[0] == 'temp_celsius'

#Check that the function produces correct answers for selected values:

# 1. What is the class value for 16.5 degrees (Celsius)?
assert temp_classifier(16.5) == 3, 'Wrong class'
print("ok :)")
# 2. What is the class value for +2 degrees (Celsius)?
assert temp_classifier(2) == 2, 'Wrong class'
print("ok :)")
# 3. What is the class value for +1 degrees (Celsius)?
assert temp_classifier(1) == 1, 'Wrong class'
print("ok :)")
# 4. What is the class value for -5 degrees (Celsius)?
assert temp_classifier(-5) == 0, 'Wrong class'
print("ok :)")