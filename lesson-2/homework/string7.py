#Ask the user to input a sentence and a word to replace. 
# Replace that word with another word provided by the user.  

a=str(input("Enter a sentence: "))
b=str(input("Enter a word to replace: "))
c=str(input("What do you want to replace with? "))

replaced_a=a.replace(b, c)

print(replaced_a)
