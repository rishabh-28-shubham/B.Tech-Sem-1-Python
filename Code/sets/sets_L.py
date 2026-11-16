a1 = [1,2,3,4]
a2 = [2,3,5,6]
def f(a1,a2):
    a1 = set(a1)
    a2 = set(a2)
    # result = (a1|a2) - (a1&a2)
    result = a1^a2
    return result

# print(f(a1,a2))


s = "The cat and the hat"

def unique_words(s):
    s = s.lower().split()
    result = len(set(s))
    return result

print(unique_words(s))