#is the short period of small anonymus function, which have multiple number of parameters but only one expression.
# syntax : lambda params : expression

#with one params
res = lambda a : a + 2
print(res(10))

#with multiple params
res = lambda a,b : a + b 
print(res(10,20))

res = lambda a,b,c : a + b + c 
print(res(10,20,30))

#in function
def addition(n):
    return lambda a : a + n 

rs = addition(3)
print(rs(10))