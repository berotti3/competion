
def base10to(n, b):
	if (int(n/b)):
		return base10to(int(n/b), b) + str(n%b)
	return str(n%b)

NK = input().split()

N = int(NK[0])
K = int(NK[1])

print(len(base10to(N, K)))

