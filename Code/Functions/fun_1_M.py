def greet(name,age):
    print("hello",name, "your age is :",age)

# greet()
# x = input("Enter your name: ")
# y = int(input("Enter your age: "))

# greet(x,y)

# def sum(x,y):

def sum(x,y):
    # print(x+y)
    return x+y

# print(sum(10,5))

y = sum(2,3)

# print(y)

# Write a function that print's the factorail of a given number


# Global keyword

x = 10

def f():
    global x
    x = 9
    print(x)

# print(x)

# f()

# print(x)

# Lambda Function

# lambda Argument : expresion

i = 10
j = 11
k = lambda i,j : i+j

print(k(i,j))

# Write a lambda fun. to perform (%) of a give number.

# Recursion

# Task print 1 -4

# Recursive fun.

# def f(n):
#     if n == 5:
#         # stop
#         return 
#     print(n)
#     f(n+1)

# f(1)

# Factorail 

def f(n):
    if n == 1 or n == 0:
        return 1
    return n * f(n-1)


f(3)