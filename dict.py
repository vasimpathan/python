# dict = Dictionary in python
# it is an unordered collection of key-value pairs within {}
# it is mutable means we can change value inside it.

a = {'id':101, 'name':'Vasim','age':34}
print(f"ID: {a['id']}")
print(f"Name : {a['name']}")
print(f"Age : {a['age']}")
print(f"Type of a : {type(a)}")
a['name'] = "Vasim Pathan"
print(f"Updated list : {a}")

# GET keys only
print(f"Extracting Keys : {a.keys()}")

# Get values only
print(f"Value of a: {a.values()}")

#Adding value
a['mobileno'] = "9156661693"
print(a)

#Update/append one dict to another
d = {'department':'IT','post':'SW'}
a.update(d)
print(a)

#To remove
a.pop('post')
print(a)