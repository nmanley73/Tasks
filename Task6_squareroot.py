# Get the square root of a positive floating point number

import math

# Insert input value as a variable
a = float(input("Please enter a positive number:"))

# Square root calculation - rounded to 2 decimals
b = round(math.sqrt(a),2)

# Print out the result
print("The square root of", a,  "is approx", b)