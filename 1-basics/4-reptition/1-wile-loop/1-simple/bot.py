print("How many cables should I remove?")
user = int(input())

cables = 1
while cables <= user:
    print("Removed cable", str(cables), "!")
    cables = cables +1
