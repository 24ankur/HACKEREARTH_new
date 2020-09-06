from collections import Counter
T=int(input())
for _ in range(T):
    N,Q=map(int,input().split())
    s=input()
    d=dict(Counter(s))
    print(d)
    for i in range(Q):
        C=int(input())
        Sum=0
        for j in d.keys():
            print(j)
            if d[j]-C>0:
                print(d[j])
                Sum=Sum+(d[j]-C)
        print(Sum)


