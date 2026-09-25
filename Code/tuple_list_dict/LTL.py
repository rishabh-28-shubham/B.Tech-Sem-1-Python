# list2 = ["Rungta",0.9,False,77]
# # print(list1)
# tuple1 = (10,20,30,40,50,60,70,80,90,100)
# # print(tuple1)
# list1 = [10,20,30,40,50,60,70,80,90,100]

# print(max(list1))
# # Adding an element at the last of list
# list1.append(110)
# print(list1)
# # insert's an element at particular position
# print(list1.insert(6,55))
# print(list1)
# print(list1.count(1))
# print(list1.index(20))

# li3 = [i for i in range(1,11)]

# print(li3)

# li4 = [i for i in range(50,101) if i%2 ==0]
# print(li4)

# li6 = [78,99,1010,"Li4",5.0]

# for i in range(len(li6)):
#     print(li6[i])

# for i in li6:
#     print(i)

st1 = ("Ravi",21,89)

name,age,per_st1 = st1
# print(name)
# print(age)
# print(per_st1)

a = 10
b = 20

a,b=b,a

print(a)
print(b)

l1 = [1,2,2,3]
t1 = (5,56,6,7)

print(tuple(l1))
print(type(tuple(l1)))
print()
print(list(t1))
print(type(list(t1)))

t2 = (56,67,99,87,31,32)
li_new = [i**3 for i in t2 if i%2 != 0]

