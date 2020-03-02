N = int(input())
S = list(input())

num = 0
result = 0

if S[N-1] ==".":
    dot = S.count(".")
    if dot > N-dot:
        result = (N-dot)
    else:
        for i in range(N):
            if S[i] == "#":
                num = i
                break
        for i in range(i,N):#  .####..
            if S[i] == ".":
                num = i
                break
        result = S[i:N].count(".")

else:
    for i in range(N-1,-1,-1):
        if S[i] == "." :
            num = i+1
            break

    white = S[0:num].count('.')
    black = S[0:num].count('#')
    if white < black:
        result = white
    else:
        result = black
print(result)

