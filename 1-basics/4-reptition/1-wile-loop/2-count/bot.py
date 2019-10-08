#allows Beep to avoid live cables

print("How many live cables should I avoid?")
user= int(input())

count = 1
while count <= user:
    print("\nAvoiding...Done!", str(count), "live cables avoided!")
    count = count + 1

print("\nAll live cables have been avoided.")