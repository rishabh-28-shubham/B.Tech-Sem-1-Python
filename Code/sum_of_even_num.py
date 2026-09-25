n = int(input())
t_e = 0

# for i in range(1,n+1):
#     if(i % 2 == 0):
#         t_e += i
# print(t_e)

# Range -> range(o,n+1,2)

for i in range(0,n+1,2):
    t_e += i
print(t_e)