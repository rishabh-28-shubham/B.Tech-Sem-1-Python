def greet():
    print("hello")

x = int(input("x : "))
y = int(input("y: "))
z = int(input("z: "))

greet()
if (x>y and x>z):
    print(f" {x}  is largest")
    greet()
elif(y>x and y>z):
    print(f" {y} is largest")
    greet()
else:
    print(f"{z} is largest")
    greet()