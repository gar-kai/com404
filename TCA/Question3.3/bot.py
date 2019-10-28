# Ask user for number of cables
print("How many miles must I travel before I reach the secret base?")
miles =int(input())


for count in range(miles, 0, -1):
    print("I have", miles, "to go before I reach the base.")
    miles =miles -1