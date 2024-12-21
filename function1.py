## important thinks for function is 
# 1. Input - inside braces - no
# 2. logic - print
# 3. output - hello world
## function is nothing but something which that we use everytime

# Defining a function
# 1. def is used to define the function

def hello():
    print("Hello World!")

# calling a function
hello()

# 2. function with params
def hello1(name):
    print(f"Hello {name}")

hello1("Vasim Pathan")

# 3. side topic of f string
country ="India"
capital = "New Delhi"
print(f"{capital} is the capital city of {country}")

# 4. function with return value

def add_number(x,y):
    #print(x+y)
    return x+y

v = add_number(5,6)
print(v)

#scope and global variable
def test(x=10):
    print(x)

test()

y = 100
def testglobal():
    # global y
    print(y)

testglobal()

n=23
def test(n):
    n=21
    print(n)

test(19)

# nested function
def test():
    print("Nested function")

def parentfun():
    test()
    print("I am parent function")

parentfun()
