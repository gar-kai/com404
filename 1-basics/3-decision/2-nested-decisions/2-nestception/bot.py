#Beep is looking for his spare battery
# Ask user where to look
print("Where should I look?")

# Read user's response
look = input()

# Display confirmation message
print("\nWhere", look + " should I look?")
look_with = input()

if (look_with == "under the bed"):
    print("\nFound some shoes but no battery")

elif (look_with == "in the bathtub"):
    print("\nFound a rubber duck but no battery")

elif (look_with == "on the table"):
    print("\nYes! I found my battery!")

else:
     print("\nI do not know where that is but I will keep looking.")
