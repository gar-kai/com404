#help the robot communicate with Beep
print("Please enter a phrase")

user=str(input())

length = len(user)
for count in range (0,length,1):
    print("Bop")
    
# Ask user for phrase
print("Please enter a phrase?")
phrase = input()

# Declare a control variable
bops = 0

# Display Bops
print()

while (bops < len(phrase)):
    print("Bop ", end="")
    bops = bops + 1
