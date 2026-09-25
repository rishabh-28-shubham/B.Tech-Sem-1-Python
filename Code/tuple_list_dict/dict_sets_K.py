# st1 = {"name":"Ravi","Age":20,"section":"K"}

# print(st1["name"])
# print(st1.get("section"))

# # for i in st1:
# #     print(i)

# # for i in st1.items():
# #     print(i)

# # for i in st1.values():
# #     print(i)


# # prd1 = {"name":"laptop1", "price":23000}
# # print(prd1)
# # prd1["price"] = 90000
# # print(prd1)
# # prd1["seller_info"] = "IT_prd"
# # print(prd1)


# students = {
#     "st1":{"name":"Ravi","ERP":909, "branch":"CSE"},
#     "st2":{"name":"Kishan","ERP":101, "branch":"CSE-AIML"}
# }


# students["st1"]["name"] = "Shivam"

# print(students)

st45 = {"name":"Ram","Age":20,"section":"K"}

st45.pop("name")
print(st45)

st45.popitem()
print(st45)

st45.clear()
print(st45)

del st45

print(st45)

stu = {
    "st1":{
        "subjects":{
            "sb1" : "maths",
            "sb2" : "Physics"
        }
    }
}