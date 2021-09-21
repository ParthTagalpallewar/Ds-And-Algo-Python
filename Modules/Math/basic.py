import math

print(math.sqrt(36))
print(math.ceil(10.2))
print(math.floor(10.2))
print(math.copysign(1, -1))
print(math.fabs(2)) # returns the distance form 
print(math.fmod(3,2))
print(math.frexp(10))
print(math.fsum([1, 2, 3]))
print(math.isfinite(math.nan))

from collections import defaultdict
d = defaultdict(list)
list1=[]

n, m = map(int,raw_input().split())

for i in range(0,n):
    d[raw_input()].append(i+1) 

for i in range(0,m):
    list1=list1+[raw_input()]  

for i in list1: 
    if i in d:
        print " ".join( map(str,d[i]) )
    else:
        print -1