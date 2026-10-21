s = input()
clean_s = s.strip()

def f(s):
    temp = ""
    for i in s:
        if i not in temp:
            temp += i
    return temp

# print(f(clean_s))

def longest_word(s):
    max_len = 0
    for i in range(len(s)):
        if len(s[i]) > max_len:
            max_len = len(s[i])
    return max_len

print(longest_word(clean_s))


