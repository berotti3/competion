
N = int(input())
A = input().split()



for i in A:
	n = int(i)
	
	if n % 2 == 0:
		if n%3==0 or n%5==0:
			continue
		else:
			print("DENIED")
			exit()

print("APPROVED")

