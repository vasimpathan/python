# Function is the block of code which perform specific task when it is called.
# in python function is defined in "def" keyword.
#without param
def hello():
    print('Hello Python')

hello()

#with param
def add(a , b):
    return a + b 

sum = add(10,20)
print(sum)

#check number is even or odd 
def checkEven(n):
    if n%2 == 0:
        print(f"{n} is even")
    else:
        print(f"{n} is odd")

checkEven(21)

#lambda function 
g = lambda x: x * x * x
print(g(10))

#lambda with filter : list the number of even number
l = [1,3,4,2,5,6,8,7,10,9]
result = list(filter(lambda x:(x%2==0),l))
print(result)

# lambda with map : multiple each number with 2
l1 = [1,2,3,4,5,6,7]
res = list(map(lambda x : (x * 2), l1))
print(res)

#reduce
from functools import reduce 
l1 = [1,2,3,4,5,6,7]
sum = reduce(lambda x,y:x+y, l1)
print(f"Reduce Final Sum : \n {sum}")