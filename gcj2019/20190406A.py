

antlist = []
for i in range(5):
    antlist.append(int(input()))
k = int(input())

for i in range(5):
    for j in range(i+1,5):
        if i==j:continue
        if antlist[j] - antlist[i] > k:
            print(":(")
            exit()

print("Yay!")