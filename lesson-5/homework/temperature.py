def convert_cel_to_far(t):
    F = round(t * 9/5 + 32, 2)
    return F

N=float(input("Enter a temperature in gradus C: "))
temp=convert_cel_to_far(N)
print(f"{N} degrees C = {temp} degrees F")

def convert_far_to_cel(f):
    C = round((f - 32) * 5/9, 2)
    return C

N1=float(input("Enter a temperature in gradus F: "))
temp1=convert_far_to_cel(N1)
print(f"{N1} degrees F = {temp1} degrees C" )