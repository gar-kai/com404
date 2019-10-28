print("Please enter a number")
factorialno= int(input())

count = factorialno -1
while count > 0:
    factorialno = factorialno*count 
    count = count -1

print("The factorial is" , str(factorialno))

# Ask user for a number
print("Please enter a number?")
number = int(input())

# Calculate factorial
count = 0
total = 1

while ( count < number ):
    count = count + 1
    total = total * count

print("The factorial is", total)
