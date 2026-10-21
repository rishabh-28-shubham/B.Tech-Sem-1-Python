s = input()
clean_s = s.strip()

# function
def check_str_palindrome(s):
    cleaned = "".join(i.lower() for i in clean_s if i.isalnum())
    return cleaned == cleaned[::-1]

print(check_str_palindrome(clean_s))
# old method

# rev = clean_s[::-1]
# if(rev == clean_s):
#     print("is a palindrome")
# else:
#     print("not a palindrome")
