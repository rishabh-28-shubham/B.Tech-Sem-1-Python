# st12 = "Hello World"

# for i in st12:
#     print(i)

# len_of_st12 = len(st12)

# for j in range(len_of_st12):
#     print(st12[j])

# st1 = "Hello World"

# print(st1[0])
# print(st1[0:5])
# print(st1[::-1])

# Reverse a string using loops
s = "hello"
for i in range(len(s)-1,-1,-1):
    print(s[i],end = " ")

# s1 = "This is topics of @"

# for i in s1:
#     if(True):
#         print(i.lower(), end="")
#     else:
#         print(i.upper(), end="")

# Check whether a Given String is a Palindrome or not.
s = "hello"
rev = ""
for i in range(len(s)-1,-1,-1):
    # print(s[i],end = " ")
    rev += s[i]
if(s == rev ):
    print("is a palindrome")
else:
    print("not a palindrome")

# Remove the spaces from the given string

s2 = "not a palindrome"

for i in s2:
    if (i!=' '):
        print(i, end = "")