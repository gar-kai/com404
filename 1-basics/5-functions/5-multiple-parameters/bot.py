def climb_ladder(NoOfStepsRemaining,NoOfStepsCrossed):
    if NoOfStepsRemaining >= NoOfStepsCrossed:
        print("Still some way to go!")
    else:
        print("We made it!")

#Calls
climb_ladder(2, 5)
climb_ladder(5, 5)