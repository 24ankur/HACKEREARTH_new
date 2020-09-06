# cook your dish here
T=int(input())
for _ in range(T):
    N,Q=map(int,input().split())
    s=input()
    temp=set(s)
    for k in range(Q):
        C=int(input())
        l1=[]
        l2=[]
        for i in temp:
            l1.append(s.count(i))


        print(l1)


        if max(l1)<=C:
            print("0")
        else:
            for i in l1:
                if (i-C)>0:
                    l2.append(i-C)

            print(sum(l2))