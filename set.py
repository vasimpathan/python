# Set in Python
# It is unordered and unindexed collection of elements enclosed within {}
# Duplicates are not allowed in set

s1 = {1, "Vasim",True,"Vasim"}
print(s1)
print(type(s1))
s1 = {1, "Vasim",True,"Vasim"} # duplicate not allowed
print(s1)


#set Operation
# 1. Update/append one dict with another
s1 = {1,2,3,4,"vasim"}
s2 = {"pathan",5,6,7}
s1.update(s2)
print(s1) # as we know it is unordered and unindex so randomly adding it.

#Updating multiple elements
s1.update([8,9,10,11,5+2j,False])
print(f"Updating multiple element : {s1}")

#Removing an element
s1.remove("pathan")
print(f"Remove : {s1}")

#union of two sets
s1.union(s2)
print(f"Union : {s1}")

#intersection of two sets \ Means return common elements
a = {1,2,3,4,5,6}
b = {6,5,7,8,9}
c= a.intersection(b)
print(f"Intersection: {c}")