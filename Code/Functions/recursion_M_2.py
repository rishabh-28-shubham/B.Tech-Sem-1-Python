# def f(n):
#     if n == 1:
#         return 1
#     if n == 2 :
#         return 2
#     return f(n-1) + f(n-2)

# print(f(5))


# a^b

def f(a,b):
    if b == 0:
        return 1
    return a*f(a,b-1)



print(f(3,2))