a=input("c: ")
a="AENIP1ELPP"
import random
import itertools
c=[]
for i in a: c.append(i)

for L in range(0, len(c)+1):
    for subset in itertools.combinations(c, L):
        print(subset)