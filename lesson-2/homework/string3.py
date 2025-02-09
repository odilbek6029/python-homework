"""Write a Python program to:
   - Take a string input from the user.
   - Print the length of the string.
   - Convert the string to uppercase and lowercase."""

a=str((input("Enter some string: ")))
print(len(a))
print(a)
a_up=""
a_low=""
for i in a:
    a_up+=i.upper()
    a_low+=i.lower()
    
print("With uppercase:b", a_up)
print("With lowercase:b", a_low)    