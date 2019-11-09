
S = list(input())
result = 0

for i in range(1,len(S)):
    if S[i] == S[i-1]:
        result = result+1
        if S[i] == "0":S[i] = "1"
        else:S[i] = "0"

print(result)