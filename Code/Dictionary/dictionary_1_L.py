word = input()

def f(word):
    empt_dict = {}

    for i in word:
        if i in empt_dict:
            empt_dict[i] +=1
        else:
            empt_dict[i] = 1
    return empt_dict

# print(f(word))
dict1 = {}
def max_val(dict1):
    max_v = (-1)*(2**32)
    for i in dict1:
        if dict1[i] > max_v:
            max_v = dict1[i]
    return 

print(max_val(dict1))


