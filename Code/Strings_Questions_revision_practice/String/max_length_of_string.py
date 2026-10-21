s = "   First programe Language"
clean_s = s.strip()

def max_len_str(str1):
    max_len = 0
    slist = str1.split()
    for i in range(len(slist)):
        if len(slist[i]) > max_len:
            max_len = len(slist[i])
    return max_len


print(max_len_str(clean_s))


