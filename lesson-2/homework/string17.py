#Ask the user for a string and replace all the vowels with a symbol (e.g., `*`). 
a=str(input("Enter a string: "))
b="aouie"
for i in b:
    a=a.replace(i, "*")


print(a)