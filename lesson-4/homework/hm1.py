#Return uncommon elements of lists. Order of elements does not matter.

s1=list(input("Enter a list: "))
s2=list(input("Enter another list: "))
s=[]
for i in s1:
    if i in s2:
        s.append(i)

print(s)        