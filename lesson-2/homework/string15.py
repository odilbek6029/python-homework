# Ask the user for a sentence and create an acronym from the first letters of each word.

a=str(input("Enter a sentence: "))
b=a.split()

acr="".join(word[0].upper() for word in b)
print(acr)