a = int(input())
b = int(input())

def exp(a,b):
    if b==0:
        return 1
    return a*exp(a,b-1)


print(exp(a,b))