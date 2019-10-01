#Beep is learning about mathematical operators
print("Please enter the first whole number")
number=(input())
print("Please enter the second whole number")
number2=(input())
print("Please enter the third whole number")
number3=(input())
evencount=0
oddcount=0
if int(number) % 2==0:
    evencount = evencount +1
else: 
    oddcount = oddcount +1
if int(number2) % 2==0:
    evencount = evencount +1
else:
    oddcount = oddcount +1
if int(number3) % 2==0:
    evencount = evencount +1
else:
    oddcount = oddcount +1

print("There were " + str(evencount) + " even and " + str(oddcount) + " odd numbers.")

