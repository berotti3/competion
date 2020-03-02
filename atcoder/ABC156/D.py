import math
def combinations_count(n, r):
	return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

def bunbo(n,r):
	return (math.factorial(n - r) * math.factorial(r))	


nab = input().split()

n = int(nab[0])
a = int(nab[1])
b = int(nab[2])

#result = 0
nfact = math.factorial(n)

#nkai = 

result = 0
fbunbo = bunbo(n,n)
for i in range(n,0,-1):
	
	result += nfact / fbunbo
		
	
	

result = result - nfact/bunbo(n,a)
result = result - nfact/bunbo(n,b)
#print(nfact)
	
print(result%(pow(10,9)+7))