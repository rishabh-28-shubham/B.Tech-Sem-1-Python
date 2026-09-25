m = int(input("Enter your marks : "))

# Check greater than 100
if(m> 100):
    print("Enter a valid value ")
else:
    if(m >=90):
        print("Grade : A")

    elif(m>=75 and m<=89):
        print("Grade : B")

    elif(m>=60 and m<=74):
        print("Grade : C")

    elif(m>=40 and m<=59):
        print("Grade : D")
    
    else:
        print("Grade : F")