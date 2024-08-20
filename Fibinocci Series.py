# Asking user for number of iterations to print with minimum of 2 iterations
Itr = input("Enter number of iterations : ")
Itr = int(Itr)

# Creating required variables and assigning initial values.
fnum = 0 # first number in the series to find
snum = 1 # second number in the series
nnum = 0 # the next number updated from the previous two number

print(fnum)
print(snum)

for i in range(2, Itr):
	i+=1
	nnum = snum + fnum # tehe next number in the series is the sum of previous two numbers
	print(nnum)
	# updating the variables as required to get the next number in the series.
	fnum = snum
	snum = nnum
