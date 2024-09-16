# simple interest
def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100


principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time (in years): "))

si = simple_interest(principal, rate, time)

print("Simple Interest:", si)
