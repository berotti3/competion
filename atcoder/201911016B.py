
N = int(input())

xy = input().split()

if N%2 == 1:
    print("No")
    exit()

for i in range(int(N/2)):
    if S[i] == S[i+(int(N/2))]:
        continue
    else:
        print("No")
        exit()

print("Yes")
