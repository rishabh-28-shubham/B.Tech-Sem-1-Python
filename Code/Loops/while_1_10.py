n = int(input("Enter a number : "))

digit = int(input("Enter a digit :"))

freq = 0

while(n!=0):
    ld = n%10
    if(ld == digit):
        freq +=1
    n //=10
    
print(f"Frequency of {digit} is {freq}")