weight = float(input("Enter weight in kilograms: "))
height = float(input("Enter height in meters: "))
bmi = (weight) / (height * height)
print("Your BMI is", bmi)
if bmi < 18.5:
    classification="underweight"
elif(bmi < 25):
    classification = "normal weight"
elif(bmi < 30):
    classification ="overweight"
else:
    classification = "obese weight"
print("Your BMI is", bmi)
print(classification)