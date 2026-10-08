n = int(input())

# Recursive function - factorail
# n X (n-1)!
def f(n):
    # Base condition
    if n == 0 or n == 1:
        return 1
    return n*f(n-1)


print(f(n))