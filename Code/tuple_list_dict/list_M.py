# l = [10,20,30,40,50,60,70]
# print(len(l))

# print(l.pop())
# print(l.remove(10))
# print(l.append(99))
# print(l.insert(4,55))
# print(l)
# # print(l.reverse())
# print(l)

# Comprehensive Method of Declaring a list
# Task is to make a list which contains no. form 1- 100
l1 = [i for i in range(1,11)]

print(l1)

# Do same for Tuple
t1 = (i for i in range(1,11))
print(t1)
# Task2 - Make list which contains only even numbers from 60 to 70.

l2 = [i for i in range(60,71) if i%2 == 0]
print(l2)

# Task3 - Create a list which contains cubes only of odd numbers from range 70 to 90.

l3 = [i**3 for i in range(70,91) if i%2 != 0]
print(l3)

# Remove duplicate elements from a list 
# Given list l = [12,34,56,78,90,23,45,12,34]

l4 = [12,34,56,78,90,23,45,12,34]

for i in l4:
    print(i)