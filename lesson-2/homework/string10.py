#Write a program that asks the user for a sentence and prints the number of words in it. 

a=str(input("Enter a sentence: "))

aa=a.replace(" ", "")
num=len(aa)

print(f"The number contains {num} word")