import copy
S = input()
S2 = copy.deepcopy(S)
K = int(input())

leng = len(S)
result = 0
flg = 0

for i in range(1,len(S)):
    print(i)
    print(S)
    if S[i] == S[i-1]:
        #print("change")
        result = result + 1
        S = S[:i] + '.' + S[i+1:]

print(S)

if S[0] == S[leng-1]:
    result = result + 1
    flg = 1

result = result * K
if flg == 1 :
    result = result - 1
print(result)

#aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
#1000000000