def sum_weight(Weight1,Weight2):
   total_weight = Weight1 + Weight2
   return total_weight

def calc_avg_weight(Weight1, Weight2):
    average_weight = sum_weight(Weight1,Weight2)/2
    return average_weight

def run():
    userinput = input ("What would you like to calculate (sum or average)?")
    if userinput == "sum": 
        Weight1= int(input("What is the weight of Beep?"))
        Weight2 = int(input("What is the weight of Bop?"))
        sum= sum_weight(Weight1,Weight2)
        print(str(sum))
    
    elif userinput == "average":
        Weight1= int(input("What is the weight of Beep?"))
        Weight2= int(input("What is the weight of Bop?"))
        average = calc_avg_weight(Weight1,Weight2)
        print(str(average))

run()
