# Ask user for the type of adventure 
print("What type of adventure should I have?")
adventure_type = input() 

# Determine what message to display
if ( (adventure_type == "scary") or (adventure_type == "short") ):
    print("\nEntering the dark forest!")
elif ( (adventure_type == "safe") or (adventure_type == "long") ):
    print("\nTaking the safe route!")
else:
    print("\nNot sure which route to take.")


