s = "Hello"
# apply strip here

def remove_duplicate(s):
    temp = "" #empty string
    for i in s:
        if i not in temp:
            temp += i
        # print(temp)
    return temp

t = (10,20,30,40,50)
# range(5) -> 0,1,2,3,4 5stop
def print_tp(t):
    for i in range(len(t)):
        # print(f"{i} : {t[i]}")
        print(i," : ", t[i])
# print_tp(t)
# print()
# print(remove_duplicate(s))

# write a function to print the min. , max. and average of all the elements present in a tuple
# Hint :-
# min()
# max()
# sum()

def min_max_avg(t):
    print(f"minimum : {min(t)}")
    print(f"maximum : {max(t)}")
    print(f"Average : {sum(t)/len(t)}")

min_max_avg(t)