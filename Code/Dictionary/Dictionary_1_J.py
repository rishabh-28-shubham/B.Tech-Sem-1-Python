# character frequency

word = "banana"

def freq_cal(word):
    empt_dict = {}

    for i in word:
        if i in empt_dict:
            empt_dict[i] +=1
        else:
            empt_dict[i] = 1
    return empt_dict

dict = {"a":-10,"b":-1,"c":-11}
# print(freq_cal(word))
def max_f(dict):
    max_value = -(1)*(2**32)

    for i in dict:
        if dict[i] > max_value:
            max_value = dict[i]
            max_key = i
    return max_key        


print(max_f(dict))