"""
1.Create a tuple of 5 colors and print them.
2.Print the first and last color using indexing.
3.Print colors from 2nd to 4th using slicing.
4.Loop through the tuple and print all colors.
5.Print the length of the tuple.
6.Check how many times "Red" appears using count().
7.Find the index position of "Blue" using index().
8.Try to add a new color using append() and see what error you get (to understand immutability)
"""
#1.Create a tuple of 5 colors and print them.
t = ("Red","Orange","Yellow","Green","Blue")
print(t)

#2.Print the first and last color using indexing.
print(f"First Index : {t[0]}")
print(f"Last Index : {t[-1]}")

#3.Print colors from 2nd to 4th using slicing.
print(f"2nd & 4th Slicing : {t[2:4]}")

#4.Loop through the tuple and print all colors.
for x in t:
    print(x)

# 5.Print the length of the tuple.
print(f"Length of t tuple : {len(t)}")

#6.Check how many times "Red" appears using count().
print(f"Num. of Red Color : {t.count('Red')}")

# 7.Find the index position of "Blue" using index().
print(f"Blue color Index : {t.index('Blue')}")

#Create a tuple with mixed data types: (10, "Hello", 5.5, True) Print each item with its data type using a loop.
a = (10, "Hello", 5.5, True)
for x in a:
    print(f"Item : {x} | Type : {type(x)}")

#8. Try to add a new color using append()
# t.append("Violet")
# print(t) #AttributeError: 'tuple' object has no attribute 'append'
