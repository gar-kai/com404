print("How many cables should I remove?")
user = int(input())

cables = 1
while cables <= user:
    print("Removed cable", str(cables), "!")
    print("\nAll live cables have been avoided.")
    cables = cables +1


