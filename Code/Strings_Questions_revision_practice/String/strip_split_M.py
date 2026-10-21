# 
# split function

# s = "Apple,Mango,Banana"
# x = s.split(",",1)
# print(x)

# write a function to find the max. length word in a given string
s = "Hello World is the very first programe for a coder in every language"
clean_s = s.strip()

def max_word(s):

    s_l = s.split()
    max_len = 0
    # s_l = ['Hello','World', 'is','the','very','first','programe','for','a','coder','in','every','language']
    for i in s_l:
        len_of_word = len(i)
        if len_of_word >= max_len:
            max_len = len_of_word

    return max_len

def rev_index(str):

    return str[::-1]
print(rev_index(clean_s))

def rev_loop(str):
    rev_temp = ""
    for i in range(len(str)-1,-1,-1):
        rev_temp = rev_temp + str[i]

    return rev_temp
print(rev_loop(clean_s))


# print(max_word(clean_s))

# programe : 8
# language : 8