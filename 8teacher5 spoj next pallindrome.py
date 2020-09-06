def rev(k):
    n = len(k)
    if k == '9' * n:
        return int(k) + 2
    dg = list(k)
    for i in range(n // 2):
        dg[-i - 1] = dg[i]
    if dg > list(k):
        return ''.join(dg)

    i = n // 2 + (0 if n & 1 else -1)
    j = n // 2

    while True:
        if dg[i] == '9':
            dg[i] = '0';
            dg[j] = '0'
            i -= 1;
            j += 1
        else:
            dg[i] = dg[j] = str(int(dg[i]) + 1)
            return ''.join(dg)


for _ in range(int(input())):
    k = input()
    print(rev(k))