#Write a program that checks if a string starts with one word and ends with another.  

a=str(input("Enter a string: "))
b=str(input("Enter a starting word: "))
c=str(input("Enter an ending word: "))

if a.startswith(b) and a.endswith(c):
    print(f"Yes, the string starts with '{b}' and ends with '{c}'.")
else:
    print(f"No, the string does not start with '{a}' and end with '{b}'.")