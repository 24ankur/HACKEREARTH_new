def check(T,x):
    x=str(x)
    for i in x:
        if i!='0' and i!='1' and i!='8':
            return "NO"




    else:
        if x==x[::-1]:
            return "YES"
        else:
            return "NO"

T=int(input())
for _ in range(T):
    x=int(input())
    print(check(T,x))


