#Read in user data
print("What is your name?")
name = input()

print("How old are you (in years)?")
age = int(input())

print("How much do you weigh (in kilograms)?")
weight = float(input())

print("How tall are you (in meters)?")
height = float(input())

#Calculate bmi
bmi = weight / (height * height) *10000


#Display result
if bmi <= 18.5:
    print(name, "you are",age, "years old and your bmi is",bmi, "which means you are underweight.")

elif bmi > 18.5 and bmi < 25:
    print(name, "you are",age, "years old and your bmi is",bmi, "which means you are normal.")

elif bmi > 25 and bmi < 30:
    print(name, "you are",age, "years old and your bmi is",bmi, "which means you are overweight.")

elif bmi > 30:
    print(name, "you are",age, "years old and your bmi is",bmi, "which means you are obese.")

else:
    print('There is an error with your input')
    




