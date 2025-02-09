#Write a program to ask for two strings and check if they are equal or not.  

a=str(input("Enter a string: "))
b=str(input("Enter another string: "))

if len(a)==len(b):
    print("They are equal!")
else:
    print("They are not equal!")