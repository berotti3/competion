N = 0

ressort = []
#c=0,j=1
def comp_list(resultlist, pos, ctime, jtime):
    if pos == N:return resultlist
    
    
    if ctime <= SElist[pos][0]:
        resultlist.append(SElist[pos])
        resultlist[-1].append(0)
        resultlist = comp_list(resultlist,  pos+1, SElist[pos][1], jtime)
    elif jtime <= SElist[pos][0]:
        resultlist.append(SElist[pos])
        resultlist[-1].append(1)
        resultlist = comp_list(resultlist,  pos+1, ctime, SElist[pos][1])

    return resultlist

T = int(input())


SElist = []

for num in range(T):

    N = int(input()) #num of activity


    for i in range(N) :
        a = list(map(int,input().split()))
        a.append(i)
        SElist.append(a)

    SElist.sort(key = lambda x: x[0])


    #Calc
    ressort = []
    resultlist1 = comp_list([] , 0, 0, 0)

    #output
    result = ""

    if len(resultlist1) != N:
        result = "IMPOSSIBLE"
    else:
        resultlist1.sort(key = lambda x: x[2])

        for i in range(N):
            if resultlist1[i][3] == 0:
                result += "C"
            else:
                result += "J"



    print("Case #" + str(num+1) + ": " + result) 

    SElist = []    
