x = int(input("x : "))
y = int(input("y: "))
z = int(input("z: "))

if (x>y and x>z):
    print(f" {x}  is largest")
elif(y>x and y>z):
    print(f" {y} is largest")
else:
    print(f"{z} is largest")