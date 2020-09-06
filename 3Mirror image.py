def check_mirror(n):
    x=0
    for i in n:
        if i=="0" or i=="1" or i=="8":
            x=True

        else:
            return "NO"
    if x:
        if n==n[::-1]:
            return "YES"
        else:
            return "NO"


for _ in range(int(input())):
    n=int(input())
    n=str(n)
    print(check_mirror(n))