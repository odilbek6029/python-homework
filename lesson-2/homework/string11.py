#Write a program to check if a string contains any digits.  

a=str(input("Enter a string: "))
aa=a.replace(" ", "")

digits="0123456789"


b = [char for char in aa if char in digits]
         
print("Digits found:", "".join(b))  # Convert list to string for better output

# Check if the string contains digits
if b:
    print("This string contains digits.")
else:
    print("This string doesn't contain digits.")