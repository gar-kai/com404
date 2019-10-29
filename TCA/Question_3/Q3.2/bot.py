print("How many heroes must we gather?")
user = int(input())

print("Gathering heroes")

heroes = 1
while heroes <= user:
    print("...Found hero", str(heroes))
    heroes = heroes +1