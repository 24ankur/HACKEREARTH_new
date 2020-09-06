from itertools import chain, combinations


def generate_subsets(a, n):
    return chain.from_iterable(combinations(a, r) for r in range(n + 1))

t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    s = int(input())
    subsets = generate_subsets(a, n)
    found = 0
    for sub in subsets:
        print(sub)
        if sum(sub) == s:
            found = True
            break
    if found:
        print("YES")
    else:
        print("NO")