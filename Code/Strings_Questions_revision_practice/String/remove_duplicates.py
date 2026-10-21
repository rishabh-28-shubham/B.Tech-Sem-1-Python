s = input()
clean_s = s.strip()

def remove_duplicates(s):
    # empty string
    temp_empty = ""
    for i in s:
        if i not in temp_empty:
            temp_empty +=i
    return temp_empty

def swapcase(s):
    te = ""
    for i in s:
        if i.isupper():
            te += i.lower()
        elif i.islower():
            te += i.upper()
        else:
            te += i
    return te

print(swapcase(clean_s))

# print(remove_duplicates(clean_s))