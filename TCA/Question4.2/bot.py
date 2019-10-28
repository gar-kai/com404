def spideySense(enemy, direction):
    if enemy == "Green Goblin":
        print("Goblin bombs incoming from front")
    
    elif enemy == "Venom":
        print("Venomous webbing incoming from behind")
    
    elif enemy == "Electro":
        print("Electro striking from left side")
    
    else:
        print("New enemy attacking from right side")


# The following are calls to the function for testing purposes
spideySense("Green Goblin", "front")
spideySense ("Venom", "behind")
spideySense ("Electro", "left side")
spideySense ("Unknown", "right side")

