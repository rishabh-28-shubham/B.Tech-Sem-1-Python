def f(a,b):
    if b ==0 :
        return 1
    return a * f(a,b-1)
print(f(2,5))