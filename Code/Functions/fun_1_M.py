# function - syntax

# def func_name():
#     //code

# Example 

def sum(x,y):
    print(x+y)

# 1. Define
# 2. function call
# 3. Execute
sum(1,2)


l = [1,2,3,4,5] #x -> l

def pl(x):
    for i in range(len(x)): #len - 5
        # i holds index value 
        print(x[i], end = " ")
    print()

pl(l)

l.append(45)
pl(l)

l.pop()
pl(l)

s = "Hello World"
pl(s)

t = (10,20,30,40)
pl(t)