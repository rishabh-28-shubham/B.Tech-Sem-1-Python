a= [1,2,3]
b = [2,3,4,5]

def unique_elements(a,b):
    a = set(a)
    b = set(b)
    result= (a|b)-(a&b)
    result = a^b
    return result

# print(unique_elements(a,b))

s = "The cat and the hat"
def unique_words(s):
    conv_s = s.lower().split()
    result  = len(set(conv_s))
    return result

print(unique_words(s))