# if_elif_else
a = 10
b = 20
if a > b:
    print("a is big then b")
else:
    print("b is big then a")

#With multiple values
a = 10
b = 20
c = 30

if (a > b) & (a > c):
    print("a is greater then b and c")
elif (b > a) & (b > c):
    print("b is greater then a and c")
else:
    print("c is greater then a and b")

#with set
s = {'Vasim','Alishan','Hasan'}
if 'Vasim' in s:
    print('Vasim is present in s set')
else:
    print('Vasim is not present in s set')

#with tuple
t = ('Wajid','Azim','Rajiya')
if 'Wajid' in t:
    print("Wajid present in t tuple")
else:
    print("Wajid not present in t tuple")

#with list
l = [1,2,3,4]
if l[2] == 4:
    print("Present at index 2 value is 3 in l list")
else:
    print("Not prsent 3 at index 2")

#with dict
d = {"k1":10,"k2":20,"k3":30}
if(d['k3'] == 30):
    print("30 is assigned to k3 keys")
else:
    print("30 is not assigned to k3 key")