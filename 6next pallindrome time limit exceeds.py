def next_pallindrome(n):
    n=n+1
    while True:
        y=str(n)
        if y==y[::-1]:
            return y
        else:
            n=n+1
for _ in range(int(input())):
    n=int(input())
    print(next_pallindrome(n))