l1 = [10,20,30,40]
t1 = (10,20,30,40)

l2 = [1,2,3,4,5,6,7,8,9,10]
print(l2[5:])
print(l2[-4])


# l3 = [i for i in range(1,1001)]
# print(l3)

t3 = (i for i in range(1,101))
print(t3)

l4 = [i for i in range(1,51) if i%2 == 0]
l5 = [55,67,98,200,101]
new_l6 = [i**3 for i in l5 if i%2!=0]

