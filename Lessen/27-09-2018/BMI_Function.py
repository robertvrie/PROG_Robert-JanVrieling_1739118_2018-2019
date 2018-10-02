def BMI(height,weight):
    BMI = (weight * 703)/height**2
    if BMI < 18.5:
        print("You are underweight (",height,",",weight,")")
    elif BMI > 25.0:
        return "You are overweight (",height,",",weight,")"
    else:
        return "Your BMI is normal (",height,",",weight,")"

heightInput = int(input("What is your height in inches?"))
WeightInput = int(input("What is your weight in pounds?"))
print(BMI(heightInput,WeightInput))