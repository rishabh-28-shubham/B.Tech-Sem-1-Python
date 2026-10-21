t = (10,20,30,40,50,60)

def swap_first_last(t):
    if len(t) == 1:
        return t
    result = (t[-1],) + (t[1:-1]) + (t[0],)
    return result

# print(swap_first_last(t))


# Rotate
def rotate(t,k):
    k = k%len(t)
    print(k)
    result = t[-k:]+t[:-k]

    return result

print(rotate(t,2))