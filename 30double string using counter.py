from collections import Counter
T=int(input())
for t in range(T):
    P=input()
    C=Counter(P)
    ans=False
    for k in C.keys():
        if C[k] > 1:
            ans=True
            break
    if ans:
        print("Yes")
    else:
        print("No")