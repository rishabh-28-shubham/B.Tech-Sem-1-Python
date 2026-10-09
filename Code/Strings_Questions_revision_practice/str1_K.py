s1 = "Recursion is very usefull"
# Split function
s2 = s1.split(" ")
print(s2)
s3 = "Apple,Mango,Banana"
s4 = s3.split(",",1)
s5 = s3.split(",",2)
print(s4)
print(s5)
s2 = s1.strip()
print(s2)

s4 = s1.lstrip()
print(f"lstrip : {s4}")

s5 = s1.rstrip()
print(f"rstrip : {s5}")