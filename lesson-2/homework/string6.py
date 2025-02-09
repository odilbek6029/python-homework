#Write a Python program to check if one string contains another.

a=str(input("Enter First string: "))
b=str(input("Enter second string: "))
aa=a.replace(" ", "").lower()
bb=b.replace(" ", "").lower()

if bb in aa:
    print(f"First String contains second string")
else :
    print(f"No, first string does not contain second string.")