from itertools import product
def subset(l1,l2):
    return list(product(l1,l2))


l2=[3,5]
l1=[1,2,3]
print(subset(l1,l2))