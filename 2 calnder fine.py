D,M,Y=list(map(int,input().split()))
d,m,y=list(map(int,input().split()))
X=D-d
U=M-m
V=Y-y

if V<0:
    print("0")
elif U<0 and V<=0:
    print("0")

else:

    if V>0:
        print("10000")
    elif U>0:
        print(500*U)
    else:
        print(15*X)
