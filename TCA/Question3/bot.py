print("How many zones must I cross?")
user=int(input())
print("Crossing zones...")


while user>0:
    print("... crossed zone " + str(user))
    user = user-1

print("Crossed all zones. Jumanji!")
