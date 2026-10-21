# t = (10,20,30,40,50,60)
t =(10,20,30,40,50)

def swap_f_l(t):
    if len(t) == 1:
        return t
    result = (t[-1],)+(t[1:-1])+(t[0],)
    return result
# print(swap_f_l(t))

def reverse(t):
    rev = t[::-1]
    return rev
# print(reverse(t))

def rotate(t,k):
    k = k%len(t)
    print(k)
    return t[-k:] +t[:-k]

print(rotate(t,2))