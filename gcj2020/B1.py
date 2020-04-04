T = int(input())


for num in range(T):

    S = input()

    output = "S"

    for i in range(len(S)):
        #print("i=" + str(i) + " " +output)
        if S[i] == '0':
            if output[-1] == "1":
                output += ")0"
            else:
                output += "0"
        else:
            if output[-1] == "0" or output[-1] == 'S':
                output +="(1"
            else:
                output += "1"
    if S[-1] == '1':
        output += ")"

    print("Case #" + str(num+1) + ": " + output[1:])     

