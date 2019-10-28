print("How many cables should I remove?")
user = int(input())

cables = 1
while cables <= user:
    print("Removed cable", str(cables), "!")
    print("\nAll live cables have been avoided.")
    cables = cables +1

# Ask user for number of cables
print("How many cables should I remove?")
cables_to_remove = int(input())

# Declare a control variable
cables_removed = 0

# Remove cables
print()

while (cables_removed < cables_to_remove):
    print("Removed cable.")
    cables_removed = cables_removed + 1
