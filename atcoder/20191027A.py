def make_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort()
    return divisors

N = int(input())

A = make_divisors(N)
result = pow(10,12)
#print(A)
for i in A:
    #print(i)
    B = (N/i-1)+(i-1)
    #print(B)
    result = min(result,B)
    
print(int(result))