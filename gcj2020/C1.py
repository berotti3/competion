N = 0

ressort = []
#c=0,j=1
def comp_list(resultlist, pos, ctime, jtime):
    if pos == N:return resultlist

    ressort.append(SElist[pos][2])
    
    if ctime <= SElist[pos][0]:
        resultlist = comp_list(resultlist+"C",  pos+1, SElist[pos][1], jtime)
    elif jtime <= SElist[pos][0]:
        resultlist = comp_list(resultlist+"J",  pos+1, ctime, SElist[pos][1])

    return resultlist

T = int(input())


SElist = []

for num in range(T):

    N = int(input()) #num of activity


    for i in range(N) :
        a = list(map(int,input().split()))
        a.append(i)
        SElist.append(a)

    #print(SElist)
    SElist.sort(key = lambda x: x[0])

    #print(SElist)

    #Calc
    ressort = []
    resultlist1 = comp_list("" , 0, 0, 0)

    #print(resultlist1)
    #print("len= " + str(len(resultlist1)))
    #output
    result = ""

    if len(resultlist1) != N:
        result = "IMPOSSIBLE"
    else:
        resultlist2 = []
        for i in range(N):
            resultlist2.append([resultlist1[i],ressort[i]])

            resultlist2.sort(key = lambda x: x[1])

        for i in range(N):
            result += resultlist2[i][0]



    print("Case #" + str(num+1) + ": " + result) 

    SElist = []    

