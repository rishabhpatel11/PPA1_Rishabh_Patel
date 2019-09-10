def bmi(feet, inches, weight):
    try:
        feet=int(feet)
    except TypeError:
        print("Expected a whole number for feet")
    try:
        inches=int(inches)
    except TypeError:
        print("Expected a whole number for inches")
    try:
        weight=float(weight)
    except TypeError:
        print("Expected number for weight")

    height=((feet*12)+inches)
    calculatedBMI=(.45*weight)/((.025*height)*(.025*height))
    calculatedBMI=round(calculatedBMI,1)

    if(calculatedBMI < 18.5):
        return [calculatedBMI, "Underweight"]

    elif(calculatedBMI < 24.9):
        return [calculatedBMI, "Normal weight"]

    elif(calculatedBMI < 29.9):
        return [calculatedBMI, "Overweight"]
        
    elif(calculatedBMI > 30):
        return [calculatedBMI, "Obese"]
