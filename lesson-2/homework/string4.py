# Write a Python program to check if a given string is `palindrome` or not.

a=str(input("Enter some number or sentence: "))
            
if a==a[::-1]:
    print("It is palindrome")
else:
    print("It is not palindrome")            
    