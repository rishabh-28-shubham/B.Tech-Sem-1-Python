def divid():
    try:
        a = int(input("Enter a number a : "))
        b = int(input("Enter a number b : "))
        print(a/b)
    except ZeroDivisionError:
        print("Can not divide by Zero")
    except ValueError:
        print("Enter a valid value")

divid()