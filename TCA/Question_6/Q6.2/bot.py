def isFusionShot (TypeofSlug1,TypeofSlug2):
    if TypeofSlug1 == TypeofSlug2:
        return True
    else:
        return False

def isDefectiveShot(TypeofSlug1,TypeofSlug2):
    if isFusionShot(TypeofSlug1,TypeofSlug2) !=True:
        if (TypeofSlug1=="Infurnus" and TypeofSlug2 == "AquaBeek") or (TypeofSlug1 == "AquaBeek" and TypeofSlug2 == "Infurnus"):
            return True
    else:
        return False

def run():
    print("Please enter the type of first slug")
    TypeofSlug1=str(input())

    print("Please enter the type of second slug")
    TypeofSlug2=str(input())

    print("Please enter fusion or defective")
    userchoice=str(input())

    if userchoice == "defective":
        defective = isDefectiveShot (TypeofSlug1,TypeofSlug2)
        print(str(defective))
    elif userchoice == "fusion":
        fusion = isFusionShot(TypeofSlug1,TypeofSlug2)
        print(str(fusion))
    else:
        print("Invalid command. Please try again")

 # Run the program
run() 