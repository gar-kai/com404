print("Please enter a number")
factorialno= int(input())

count = factorialno -1
while count > 0:
    factorialno = factorialno*count 
    count = count -1

print("The factorial is" , str(factorialno))