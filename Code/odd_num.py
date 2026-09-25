n = int(input())

t_odd = 0
for i in range(1,n+1):
    if(i % 2 != 0):
        t_odd += i

print(t_odd)

t_odd2 = 0
for i in range(1,n+1,2):
    t_odd2 += i
print(t_odd2)