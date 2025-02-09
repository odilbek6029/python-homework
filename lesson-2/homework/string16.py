#Write a program that asks the user for a string and a character, 
# then removes all occurrences of that character from the string. 

a=str(input("Enter a string: "))
b=str(input("Enter a character: "))
aa=a.replace(b, "")

print(aa)