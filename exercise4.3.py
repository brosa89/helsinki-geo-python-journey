from temp_functions import fahr_to_celsius, temp_classifier

temp_data =  [19, 21, 21, 21, 23, 23, 23, 21, 19, 21, 19, 21, 23, 27, 27, 28, 30, 30, 32, 32, 32, 32, 
              34, 34, 34, 36, 36, 36, 36, 36, 36, 34, 34, 34, 34, 34, 34, 32, 30, 30, 30, 28, 28, 27,
              27, 27, 23, 23, 21, 21, 21, 19, 19, 19, 18, 18, 21, 27, 28, 30, 32, 34, 36, 37, 37, 37, 
              39, 39, 39, 39, 39, 39, 41, 41, 41, 41, 41, 39, 39, 37, 37, 36, 36, 34, 34, 32, 30, 30,
              28, 27, 27, 25, 23, 23, 21, 21, 19, 19, 19, 18, 18, 18, 21, 25, 27, 28, 34, 34, 41, 37, 
              37, 39, 39, 39, 39, 41, 41, 39, 39, 39, 39, 39, 41, 39, 39, 39, 37, 36, 34, 32, 28, 28,
              27, 25, 25, 25, 23, 23, 23, 23, 21, 21, 21, 21, 19, 21, 19, 21, 21, 19, 21, 27, 28, 32,
              36, 36, 37, 39, 39, 39, 39, 39, 41, 41, 41, 41, 41, 41, 41, 41, 41, 39, 37, 36, 36, 34,
              32, 30, 28, 28, 27, 27, 25, 25, 23, 23, 23, 21, 21, 21, 19, 19, 19, 19, 19, 19, 21, 23,
              23, 23, 25, 27, 30, 36, 37, 37, 39, 39, 41, 41, 41, 39, 39, 41, 43, 43, 43, 43, 43, 43,
              43, 43, 43, 39, 37, 37, 37, 36, 36, 36, 36, 34, 32, 32, 32, 32, 30, 30, 28, 28, 28, 27,
              27, 27, 27, 25, 27, 27, 27, 28, 28, 28, 30, 32, 32, 32, 34, 34, 36, 36, 36, 37, 37, 37,
              37, 37, 37, 37, 37, 37, 36, 34, 30, 30, 27, 27, 25, 25, 23, 21, 21, 21, 21, 19, 19, 19,
              19, 19, 18, 18, 18, 18, 18, 19, 23, 27, 30, 32, 32, 32, 32, 32, 32, 34, 34, 34, 34, 34,
              36, 36, 36, 36, 36, 32, 32, 32, 32, 32, 32, 32, 32, 30, 30, 30, 30, 30, 30, 30, 30, 30,
              30, 30, 30, 30, 28, 28]

temp_classes = []

for temp in temp_data:
    temp_celsius = fahr_to_celsius(temp)
    temp_class = temp_classifier(temp_celsius)
    temp_classes.append(temp_class)

zeros = temp_classes.count(0)
ones = temp_classes.count(1)
twos = temp_classes.count(2)
threes = temp_classes.count(3)

print(len(temp_data))
print(len(temp_classes)) #temp_classes and temp data should be the same
print(f"There are {zeros} temperature values classified as zero, {ones} classified as one, {twos} classified as 2 and {threes} classified as 3.")

import inspect

# Check that functions are in the namespace
assert inspect.isfunction(fahr_to_celsius)
assert inspect.isfunction(temp_classifier)
# Check that variable has been created
assert 'temp_celsius' in locals()
assert 'temp_class' in locals()
assert 'temp_classes' in locals()

# Check that temp_classes is a list
assert type(temp_classes) == list
# Check that the functions have a single parameter
t_params = list(inspect.signature(temp_classifier).parameters.keys())
f_params = list(inspect.signature(fahr_to_celsius).parameters.keys())
assert len(t_params) == 1
assert len(f_params) == 1

#Check that required variables exists and print their value (check manually that the answers make sense!):

# Check the variable "zeros" 
assert 'zeros' in locals()
print(zeros)
# Check the variable "ones" 
assert 'ones' in locals()
print(ones)
# Checkthe variable "twos" 
assert 'twos' in locals()
print(twos)
# Check the variable "threes" 
assert 'threes' in locals()