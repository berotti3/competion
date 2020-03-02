
N = int(input())
Xs = input().split()

X =[]
for i in Xs:
	X.append(int(i))

minnum = 10000000000

for i in range(101):
	sumnum = 0
	for j in X:
		sumnum += (i-j)*(i-j)
	
	minnum = min(sumnum,minnum)

print(minnum)
		
	
		
	