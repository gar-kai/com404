def is_league_united(Hero1,Hero2):

    if Hero1 == "Superman" and Hero2 == "WonderWoman":
        return True
    else:
        return False

def decide_plan(Hero1,Hero2):
    united = is_league_united(Hero1,Hero2)
    if united == True:
        return "Time to save the world!"
    else:
        return "We must unite the league!"
    
def run():
    print("Enter the name of the first hero")
    hero1=str(input())
    
    print("Enter the name of the second hero")
    hero2=str(input())

    print("Please enter league or plan")
    userchoice=str(input())

    if userchoice == "league":
        united = is_league_united(hero1,hero2)
        print(str(united))
    elif userchoice == "plan":
        plan = decide_plan(hero1,hero2)
        print(str(plan))
    else:
        print("Invalid command. Please try again")

# Run the program
run()