principal_amount = 10000
interest_rate = 10
time_period = 20

accumalated_amount: int = 0

for i in range(1,time_period+1):
	principal_amount += principal_amount*(interest_rate/100)
	print(principal_amount)
	print()