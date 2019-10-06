# ask user what type of book cover
print("What type of cover does the book have?")
book = input()
    
# decide if the book cover is soft or hard
if (book == "soft"):

    # ask user what to play with
    print("\nIs this book perfect bound?")
    soft_with = input()
    
    # decide if beep should play with toys or friend
    if (soft_with == "yes"):
        print("\nSoft cover, perfect bound books are very popular!")
    else:
        print("\nSoft covers with coils or stitches are great for short books")
else:
    print("\nBooks with hard covers can be more expensive!")