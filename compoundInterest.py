investment = input("Enter your investment amount: ")
rate = input("Enter rate of investment return: ")
time  = input("Enter the time for investment to terminate: ")

investment = float(investment)
rate = float(rate)
time = int(time)

for i in range(1, time + 1):
    investment = investment + (investment * (rate/100))
    
print(f"Your investment after {time} year(s) = ${investment:.2f}")

