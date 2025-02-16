def invest(amount,rate,years):
    for i in range(years):
        amount=amount*(1+rate)
        print(f"year {i+1}: $", round(amount,2))

amount=float(input("Enter an initial amount $: "))
rate=float(input("Enter an annual percentage rate: "))
years=int(input("Enter a number of years: "))
invest(amount,rate,years)