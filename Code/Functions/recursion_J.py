# def func(n):
#     if n == 4:
#         return
#     print(n)
#     func(n+1)

# func(1)


def facto(n):
    if n == 1 or n == 0:
        return 1
    return n*facto(n-1)

print(facto(5))