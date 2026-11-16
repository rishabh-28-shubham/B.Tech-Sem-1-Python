s = input()

def count_freq(s):
    temp_dict = {}
    for i in s:
        if i not in temp_dict:
            temp_dict[i] = 1
        else:
            temp_dict[i] += 1
            
    return temp_dict


print(count_freq(s))