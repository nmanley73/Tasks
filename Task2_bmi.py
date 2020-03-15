# Program calculates somebody's BMI

# Create Variables and input values
Weight = float(input("Enter weight:"))
Height = float(input("Enter height:"))

# Calculate BMI
BMI = Weight / ((Height/100)**2)

# Print out result
print("BMI is", round(BMI,2), "metres squared")