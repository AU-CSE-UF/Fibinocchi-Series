Itr = input("Enter number of iterations : ")
Itr = int(Itr)

fnum = 0
snum = 1
nnum = 0

print(fnum)
print(snum)

for i in range(2, Itr):
	i+=1
	nnum = snum + fnum
	print(nnum)
	fnum = snum
	snum = nnum