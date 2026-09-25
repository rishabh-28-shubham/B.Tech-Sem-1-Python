n = int(input())

# counter
count = 0

for i in range(1,n+1):
    if(n%i == 0):
        count += 1

# check for prime
if(count == 2):
    print(f"Given number {n} is a Prime number")
else:
    print(f"Given number {n} is not a Prime number")