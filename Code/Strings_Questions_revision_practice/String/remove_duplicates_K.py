s = input()
clean_s = s.strip()


def remove_dup(s):
    # Decalre empty string
    temp= ""
    for i in s :
        if i not in temp:
            temp += i
    return temp

def count_longest(s):
    max_len = 0
    # split
    sl = s.split()
    for i in range(len(sl)):
        if len(sl[i]) > max_len:
            max_len = len(sl[i])
    return max_len

print(count_longest(clean_s))

# print(remove_dup(clean_s))

