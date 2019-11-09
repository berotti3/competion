import copy
S = input()
K = int(input())

leng = len(S)
result = 0
flg = 0
skp=0

for i in range(1,len(S)):
    if skp==1:
        skp=0
        continue
    #print(i)
    #print(S)
    #print(S[i])
    #print(S[i-1])
    if S[i] == S[i-1]:
        result = result + 1
        S = S[:i-1] +"."+ S[i:]
        skp = 1
        
#print(S)

if S[0] == S[leng-1]:
    result = result + 1
    flg = 1

result = result * K
if flg == 1 :
    result = result - 1
print(result)

#aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
#1000000000