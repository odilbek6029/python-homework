#Write a program that counts the number of vowels and consonants in a given string.

a=str(input("Enter some sentences: "))

aa=a.replace(" ", "").lower() #remove space 

vowels="aouie"
# initial values of vowels and consonants
v_num=0
c_num=0

for j in aa:
        if j in vowels:
            v_num=v_num+1
        else:
            c_num=c_num+1


print("Number of vowels are {num}".format(num=v_num))
print(f"Number of consonants are {c_num}")