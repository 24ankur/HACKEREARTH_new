for __ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    s = int(input())
    f = 0
    for i in range(2 ** n):
        c = 0
        for j in range(0, n):
            if (i & (1 << j)):
                c += a[j]
        if c == s:
            print("YES")
            f = 1
            break
    if f == 0:
        print("NO")

3