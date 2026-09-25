laptop1 = {"name":"Asus Tuf",
    "RAM":"12GB",
    "Storage":"1TB"
}

# print(laptop1["name"])
# print(laptop1.get("RAM"))

stu1 = {"name" : "Parmanand","ERP":1184, "Branch" : "CSE", "Section":"M"}

# stu1.pop("Section")
# print(stu1)
# stu1.popitem()
# print(stu1)
# stu1.clear()
# print(stu1)
# del stu1
# print(stu1)

# for i in stu1.keys():
#     print(i)

# for i in stu1.items():
#     print(i)

# for i in stu1.values():
    # print(i)
# stu1["phone_number"] = 78459643
# stu1["Section"] = "L"
# print(stu1)




# print(stu1["name"])
# print(stu1.get("ERP"))


# Nested Dict.
students = {
    "Stu1":{"name":"R", "Section":"L","ERP":11223,"Branch":"AI-ML"},
    "Stu2":{"name":"A", "Section":"K","ERP":15864,"Branch":"AI-DS"}
}

students["Stu2"]["address"] = "S-1, Rungta hostel -12"
students.popitem()
print(students)

# ERP 01613
