def under(words):
    print(word)
    line = ""
    for num in range(0,len(word)):
        line = line + "*"
    print(line)

def over(words):
    line = ""
    for num in range(0, len(word)):
        line = line + "*"
    print(word)

def both(words):
    line = ""
    for num in range(0,len(word)):
        line = line + "*"

def grid(words, size):
    WordLine = ""
    Line = ""

    LineLong = ""
    for number1 in range(0,len,words):
        Line = Line + "*"
    
    for number2 in range(0,size):
        LineLong = LineLong + Line +"    "
        if number2 == size -1:
            WordLine =WordLine + words
        else:
            WordLine = WordLine + word + " | "

    for number3 in range(0,size):
        print(LineLong)
        print(WordLine)
    
    print(LineLong)

def options():
    print("Type a word: ")
    word=input()
    print("Please choose one of the options shown below")
    print("Option 1: under")
    print("Option 2: over")
    print("Option 3: both")
    print("Option 4: grid")


options()
option = str(input())

if option not in ["1","2","3","4"]:
    print("Invalid option")
    print()
    options()

if option ==1:
    str(under(word)
elif option==2:
    over(word)
elif option==3:
    both(word)
elif option==4:
    size = int(input())
    print("What size grid?")
    grid(word,size)
else: 
    print("Invalid option")