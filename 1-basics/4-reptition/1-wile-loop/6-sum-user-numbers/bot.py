#Bop retrieve some numbers and calculate their sum

notoadd=int(input("How many numbers should I sum up?"))

numberadding=0
sum=0
temp=0
while numberadding < notoadd:
    for count in range (1, notoadd+1,1):
         print("Please enter number "+ str(count)+ "of" + str(notoadd))
         temp = int(input())
         sum = sum + temp
         
    print("The answer is" +str(sum))