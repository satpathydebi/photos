from re import S


def reverse(s):
    s=s.split(" ")          # convert to list 
    #s.reverse()
    s=' '.join(map(str,s[::-1]))     # convert to string 
    print(s)
s="Hello World"
#reverse(s)
A= [3,1,2,8,4,5 ]
A.sort()
for i in range(1,A.pop()):
    if i not in A:
        #print(i)
        pass

import copy

def print_all_sum_rec(target, current_sum, start, output, result):
 if current_sum == target:
   output.append(copy.copy(result))

 for i in range(start, target):
   temp_sum = current_sum + i
   if temp_sum <= target:
     result.append(i)
     print_all_sum_rec(target, temp_sum, i, output, result)
     result.pop()
   else:
     return

def print_all_sum(target):
 output = []
 result = []
 print_all_sum_rec(target, 0, 1, output, result)
 return output


n = 4
res = print_all_sum(n)
print(res)
