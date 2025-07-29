# List is the ordered collection of element enclosed within square brancket []
# It is mutable means we can change value in it [Elements are not permanant]
item = ['vasim',"wajid","azim","1","2","3"]

print("Print all the element from the list")
print(item)

print("\nGet particular element from list:")
print(item[2])
print(item[5])
print(item[-1])

print("\nSlice the list")
print(item[0:3])
print(item[2:])

print("\nTo add the element to the end of the list- append")
item.append("Alishan")
item.append("hasan")
item.append("xyz")
item.append("pqr")
print(item)

print("\nTo update the element in the list - indexKey")
item[8] = "ABC"
print(item)

print("\nTo remove the element from the list - remove")
item.remove("pqr")
print(item)
item.pop()
print(item)

print("\nTo clear or empty the list - clear")
item.clear()
print(item)

#Revering element
a = [2,1,3,5,4,6]
b = ['d','c','b','a']
a.reverse()
print(f"Reverse Element : {a}")
a.sort()
print(f"Ascending Sort : {a}")
b.sort()
print(f"Ascending Sort : {b}")

#Insert Element to specified index
a.insert(1,"Vasim")
print(f"Newly Added Element at index 1 : {a}")

# Concatenate
print(a + b)

#Repeatation
print(b*3)