# Create a program that takes a number and checks if it’s even or not.

a=int(input("Enter the number: "))

b=a%2

if b==0:
    print("{a} is even number.".format(a=a))
else:
    print(f"{a} is odd number.")