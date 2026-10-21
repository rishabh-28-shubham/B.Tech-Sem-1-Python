# s = "ABABA"
# rev  = s[::-1]

# if rev == s :
#     print("palindrome")
# else:
#     print("Not a palindrome")

s = "keshav.kumar@rungta.org"
s1 = s.split("@",1)[1]
print(s1)
# Write program to split the string at first 2 colones only 
#  "name:age:city:country"

#parse the given string ; s = "   name:Ram erp:00112 section:K"

s1 =  "   python    is   high level   programming   "
x = s1.strip()
y = x.split(" ")
temp = ""
for i in y:
    if i != "":
        temp += i + " "

print(temp)
