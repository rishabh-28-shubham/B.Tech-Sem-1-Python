t = tuple()
# t = (10,)
def swap(t):
    if len(t) < 2:
        return t
    result = (t[-1],) + (t[1:-1]) + (t[0],)
    return result
# print(swap(t))
def rotate(t,k):
    # Edge case
    k = k%len(t)
    print(k)
    return t[-k:] + t[:-k]

print(rotate(t,2))