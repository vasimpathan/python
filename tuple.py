# tuple is the ordered collection of elements which is enclosed within round bracket()
# It is immutable means once the value set we can not change or cannot reassignment.

a = (1,3.14,"Vasim Pathan",5-2j,True)
print(a)

#To get the first value from tuple
print(a[0])

#To get the 3rd element
print(a[2])

#To get the last element
print(a[-1])

#To get the 2 element from and to 
print(a[1:3])



#immutable : we can not modify the any element value 
# a[1]=200
# print(a) # it will give type error : TypeError: 'tuple' object does not support item assignment

# To get the lenght of list
print(len(a))

#To concatnate us + 
a = (1,2,3)
b = (4,5,6)
print(a + b) # joined b to end of a 
print(b + a) # Append a to end of b

# Repeat tuple element
a = ("vasim","786")
b = ("Pathan",34)
print(a*3) # ('vasim', '786', 'vasim', '786', 'vasim', '786')

print(a*3 + b)

# Maximum and minimum
a = (1,2,3,4,5,6)
print(f"Min - {min(a)}")
print(f"Max - {max(a)}")