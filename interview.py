def upper_str(a):
    def wrapper():
        x=str.upper(a)
        print(x)

@upper_str("abc")

#def cal(a,b):
#    x=lambda a,b:a*b
#    return x
#print(type(b(1,2)))


x=["Sam", [10987, [2.0, ["Hi", 39]], "Hello12345"], [[[56, 10.345678, ["He!!0"]]]]]
for i in x:
    if type(i) is str:
        print(i)
    elif type(i) is list:
        for j in i:
            if type(j) is int:
                print(j)
            elif type(j) is list:
                for k in j:
                    if type(k) is float:
                        print(k)