#Write a program that asks the user for a string 
# and prints the first and last characters of the string.

a=str(input("Enter a sentence: "))
aa=a.replace(" ", "").lower()

first=a[0]
last=a[len(a)-1]
print(f"First character is {first} and the last one is {last}")