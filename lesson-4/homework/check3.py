s=str(input("Enter a string: "))
s.lower
vowels="aouie"
st=""
count=1
for i in range(len(s)):
    if count%3==0 and i!=len(s)-1 and s[i] not in vowels:
            vowels+=s[i]
            st+=s[i]+"_"
            #count+=1
    else:
          st+=s[i]
          count+=1


print(st)