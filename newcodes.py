a = int(input("enter the first number:" ))
b = int(input("enter the second number: "))
c = int(input("enter the third number: "))

if(a >= b and a >= c):
    print("first number is largest:", a)
elif(b>=c):
    print("second the number: ", b)
else:
    print("third is largest", c)