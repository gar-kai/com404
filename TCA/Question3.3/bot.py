# Ask user for number of cables
print("How many miles must I travel before I reach the secret base?")
cables_to_avoid = int(input())



for count in range(cables_to_avoid, 0, -1):
    print("I have", cables_to_avoid, "to go before I reach the base.")
    cables_to_avoid = cables_to_avoid -1