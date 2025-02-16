
def factorize(n):
    
    for i in range(1,n):
        if n%i==0:
            print(f"{i} is a factor of {n}")
        

n=int(input("Enter a number you want to factorise: "))
factorize(n)