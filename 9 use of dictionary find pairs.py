def pairs(a, k):

    d = {}
    answer = 0
    for i in a:
        d[i] = i

    print(d)
    for j in a:
        g = j+k
        if g in d:
            answer +=1
    return answer

n,k=map(int,input().split())
a=list(map(int,input().split()))
print(pairs(a,k))
