
AB = input().split()
A = int(AB[0])
B = int(AB[1])
result =0

for i in range(2):
    if A>B:
        result = result+A
        A = A-1
    else:
        result = result+ B
        B = B-1

print(result)
