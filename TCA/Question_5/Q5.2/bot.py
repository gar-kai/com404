print("Welcome to the Planet of the Apes...")

human=0
ape=0
for count in range (0,7,1):
    print("...be ye human or be ye ape?")
    user=str(input())

    if user == "Human":
        human=human +1
        print("I did not start this war. But I will finish it.")
    
    elif user == "Ape":
        ape=ape +1
        print("Apes together strong!")

    else:
        print("This is not your fight.")

    
print("Total humans encountered:", human) 

print("Total apes encountered:", ape)