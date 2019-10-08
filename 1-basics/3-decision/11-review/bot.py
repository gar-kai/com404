#Decisions with if...elif...else statements
#Beep learning colours

print("1.Red")
print("2.Blue")
print("3.Green")
print("4.Yellow")

Choice= int(input ("\n Select the number of your favorite colour:" ))

if (Choice==1):
    print("You choose Red!")
elif (Choice == 2):
    print("You choose Blue!")
elif (Choice==3):
    print("You choose Green!")
elif (Choice==4):
    print("You choose Yellow!")
else:
    print("You made an invalid choice")


#Multiple conditions with logical (AND, OR and NOT operators)
#Beep indentifying shapes 
# Retrieve shape from user
print("What shape do I have?")
shape = input()
    
# Identify the shape
if ((shape == "square") or (shape == "rectangle") or (shape == "rhombus")):
    print("This shape is a parallelogram.")
else:
    print("This shape is not a parallelogram.")

#Nested decisions
# ask user what to do
print("What should I do (play/study)?")
activity = input()
    
# decide if beep should play or study
if (activity == "play"):

    # ask user what to play with
    print("What should I play with (toy/friend)?")
    play_with = input()
    
    # decide if beep should play with toys or friend
    if (play_with == "toy"):
        print("I will play with my toys!")
    else:
        print("I will play with my friend!")
else:
    print("I will study")