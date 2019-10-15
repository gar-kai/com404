def display_ladder(NoOfStepsLadder):
    for count in range (0, NoOfStepsLadder,1):
        print("| |")
        print("***")

def create_ladder():
    print("How many steps remain?")
    steps = int(input())
    display_ladder(steps)

#call
create_ladder()
