import time
a="apple"
print(list(a)[::-1])
str_join=''.join([str(elem) for elem in (list(a)[::-1])])
print(str_join)
str_join_1=""
for i in (list(a)[::-1]):
    str_join_1+=i
print(str_join_1)
#print(a.lstrip())
cu_tm=time.localtime(time.get_clock_info())
print(cu_tm)
a = lambda x, y : x*y
print(a(7, 19))