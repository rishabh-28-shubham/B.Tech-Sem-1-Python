# # Write a function to reverse a given tuple
# t = (10,20,30,40)
# # output 
# # (40,30,20,10)

# def rev_t(t):
#     return t[::-1]
# # print(rev_t(t))
# # i = int(input("Enter the index you want to remove"))

# def remove_at(t,i):
#     return t[:i] + t[i+1:]

# # print(remove_at(t,i))

# t = (10,20,30,40,50)
# # k =2
# # output : (40,50,10,20,30)

# def f(t,k):
#     return t[-k:] + t[:-k]

# print(f(t,2))

# #Q1 write a function check what elements gives the Target sum in the given list :
# # Sample test case : 
# # target = 9
# # L = [1,2,3,1,4,5,8]

l = [0,1,0,3,12]

def f(l):
    non_zero = [i for i in l if i!=0]
    zero = [i for i in l if i==0]
    print(non_zero + zero)

f(l)