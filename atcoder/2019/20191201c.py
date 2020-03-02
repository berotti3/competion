
X = int(input())

N = X/100 #個数

Xn = X%100
#print("Xn="+str(Xn))
n = 0

N5 = int(Xn/5)
#print("N5="+str(N5))
N4 = int(Xn%5/4)
#print("N4="+str(N4))
N3 = int((Xn-N5*5-N4*4)/3)
#print("N3="+str(N3))
N2 = int((Xn-N5*5-N4*4-N3*3)/2)
#print("N2="+str(N2))
N1 = Xn-N5*5-N4*4-N3*3-N2*2

#print(N1)

if N5+N4+N3+N2+N1>N:
    print("0")
else:
    print("1")



