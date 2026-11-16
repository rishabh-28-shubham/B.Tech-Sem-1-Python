word = "banana"

def count_freq(word):
    empty_dict = {}

    for i in word:
        if i in empty_dict:
            empty_dict[i] +=1
        else:
            empty_dict[i] = 1
    return empty_dict


# print(count_freq(word))
dict1 = {"a":-11,"b":-1,"c":-4}
def max_key(dict):
    max_val = -1*(2)**(32)
    for i in dict:
        if dict[i] > max_val:
            max_val = dict[i]


print(max_key(dict1))