t = (10,20,30,40)

def min_max_avg(t):
    print(f"Maximum : {max(t)}")
    print(f"Minimum : {min(t)}")
    print(f"Average : {sum(t)//len(t)}")

min_max_avg(t)
# 0 1 2 3
def f(t):
    for i in range(len(t)):
        # print(f"{i} : {t[i]}")
        print(i," : ",t[i])
# f(t)

