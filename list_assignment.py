"""
Concepts to Practice:
- Creating lists
- Indexing, slicing
- Adding/removing items
- Sorting, reversing
- List methods: append, insert, remove, pop, sort, reverse, len
"""
# 1. Create a list of 5 animals and print it.
l = ['Tiger','Lion','Elephant','Fox','Deer']
print(l)

# 2. Print the first and last animal using indexing.
print(f"First Index : {l[0]} & Last Index : {l[-1]}")

# 3. Print animals from 2nd to 4th using slicing.
print(f"2nd and 4th Slicing Animal : {l[2:4]}")

# 4. Add a new animal at the end 
l.append("Dog")
print(l)

# 5. Print the total number of animals using len().
print(f"Length : {len(l)}")

#6. Sort the list alphabetically using sort().
l.sort()
print(f"Sort List : {l}")

#7. Reverse the list using reverse().
l.reverse()
print(f"Reverse : {l}")

#8. Add an animal at position 2 using insert().
l.insert(2,"Cat")
print(l)

#9. Remove an animal by name using remove().
l.remove("Cat")
print(l)

#10. Remove the last animal using pop().
l.pop()
print(l)

a = [100, 50, 25, 75, 150]
# Sort numbers in ascending and descending order.
a.sort()
print(f"Ascending Order : {a}")
a.reverse()
print(f"Decending Order : {a}")

# Find the maximum and minimum number.
print(f"Max Val : {max(a)} & Min Val : {min(a)}")

# Calculate the sum of all numbers using a loop.
sum = 0
for n in a:
    sum +=n
    
print(f"Sum of all number : {sum}")