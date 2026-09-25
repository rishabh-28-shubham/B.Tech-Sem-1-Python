dict1 = {"Stu_name":"Rudra","Age":17,"Percentage":55.0}

print(dict1)

for key in dict1:
    print(key)
print()
for i in dict1.items():
    print(i)

print(dict1.get("Stu_name"))
print(dict1["Stu_name"])