# Ask user for the type of adventure 
print("What type of book is this?")
adventure_type = input() 

# Identify the type of book
if ((adventure_type == "scary") or (adventure_type=="short")):
    print("\nEntering the dark forest")

if ((adventure_type == "safe") or (adventure_type=="long")):
    print("\nTaking the safe route!")

else:
    print("Not sure which route to take")


