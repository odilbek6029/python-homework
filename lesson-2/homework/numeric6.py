#Create a program that accepts a number and returns the last digit of that number.

a=int(input("Enter the number: "))

my_str=f"{a}"
print("the last digit is ", my_str[len(my_str)-1])