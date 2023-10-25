from operator import index, indexOf
from re import S
from typing import Counter


weekdays = ['sun','mon','tue','wed','thu','fri','sat']
listAsString = ' '.join(weekdays)
#print(listAsString)
listAsTuple = tuple(weekdays)
#print(listAsTuple)
a=[1,2,3]
l=','.join(map(str,a[::-1]))
#print(l)
#for i in a:
    #print(a[-i])
names = ['Chris', 'Jack', 'John', 'Daman']
#print(names[-1][2])
names=["cat","dog","god","tca"]
b=[]
for i in names:
    sort=''.join(sorted(i))
    if sort in b:
        b.append(sort)
    else:
        b.append(sort)
d=Counter(b)


def calc(A,target):
    b=set()
    x=[]
    for i in range(len(A)):
        for j in range(len(A)):
            for k in range(len(A)):
                if A[i]+A[j]+A[k] == target:
                    b.add(A[i])
                    b.add(A[j])
                    b.add(A[k])
            print(b)
        x.append(b)
    #print(x)

A=[1, 1, 0, -1, -2]
target=0
calc(A,target)
            
