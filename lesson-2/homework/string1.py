#Create a program to ask name and year of birth from user and tell them their age.

a=input("Hello! What's your name?")
b=int(input("what is your date of birth?"))

age=2025-b
print("{name}, your age is {age}, you look younger than that".format(name=a, age=age))