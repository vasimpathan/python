fname = "vasim"
lname = "pathan"
print(fname + " "+ lname)
print(f"My fullname is {fname + ' '+ lname}")

# Complex number
j=1.2 - 2.3j
print(j)
print(j.real, j.imag)

# Dynamic Typing : we can easily change data type of same variable.
a=10
a="Vasim"
print(a)

# Strong typing : its means we can not concatnate string + number
a="Vasim"
#print(a+1) ## will throw error
print(a+str(1))

# String Fomating
a = 100
print("The value of a is",a) # simple format 
fname = "Vasim"
lname = "Pathan"
print("My first name is {} and last name is {}".format(fname,lname))
print("My first name is {0} and last name is {1}".format(fname,lname))
print("My first name is {1} and last name is {0}".format(lname,fname)) # if we changed variable
print("My first name is {a} and last name is {b}".format(a=fname,b=lname))

# Input Type
a = input("Enter the value of a: ")
b = input("Enter the value of b:")
sum = int(a) + int(b)
print(f"Sum of a + b is "+str(sum))


