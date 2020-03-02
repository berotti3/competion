
NR = input().split()

N = int(NR[0])
R = int(NR[1])

if N>=10:
	print(R)
else:
	print(R+(100*(10-N)))