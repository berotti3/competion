T = int(input())


for num in range(T):

    S = input()

    output = ""
    oldnum = 0

    for i in range(len(S)):
        
        
        nownum = int(S[i])

        knum = oldnum - nownum

        if knum < 0 :
            output += '(' * (knum * -1)


        if knum > 0 :
            output += ')' * (knum)
        
        output += S[i]

        oldnum = nownum

        #print("i=" + str(i) + " " +output)

    output += ')' * oldnum


    print("Case #" + str(num+1) + ": " + output)     

