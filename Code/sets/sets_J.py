s = "The cat and the hat"

def unique_words(s):
    x = s.lower().split()
    y = set(x)
    print(y)
    print(len(y))

unique_words(s)