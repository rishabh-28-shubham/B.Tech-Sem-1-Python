
x = input()
y = input()
def divide(a,b):
    try:
        a = int(a)
        b = int(b)
        print(a/b)
    except ZeroDivisionError:
        print(f"given input denominator b should not be Zero")
    except ValueError:
        print("Input value should be whole number")

divide(x,y)