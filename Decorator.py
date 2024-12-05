def fun1(x):
    def fun2(p,q):
        p=p+5
        q=q+10
        data =x(p,q)
        return data
    return fun2
@fun1
def main_function(x,y):
    return x+y
x=main_function(5,10)
print(x)
