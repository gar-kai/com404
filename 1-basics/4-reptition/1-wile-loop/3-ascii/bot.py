#display a message
print("How many bars should be charged?")
user = int(input())

cable=0
while cable < user:
    print("\nCharging:", end ="")
    for count in range (0,cable, 1):
        print( "█ ", end ="")
    
    print("")

    cable = cable + 1

if cable == user:
    print("The battery is fully charged.")



