from itertools import combinations


def is_possible_set_sum(numbers, N):
    # One of those rare cases where range() is ok!
    for r in range(2,len(numbers)+1):
        for combo in combinations(numbers, r):
            print(combo)
            if sum(combo) == N:
                return "subset is available"
    return "subset is not availale"



n = int(input())
a=list(map(int,input().split()))
s = set(a)
N=int(input())

print(is_possible_set_sum(s,N))