# Looping statements are used to repeat a task multiple times.
#1. For Loop
for x in range(1,10):
    print(f"For loop number : {x}")

#2. While Loop 
x = 2
n = 1
while n <=10:
    print(f"{x} * {n} = { x * n}")
    n = n+1

#assignment 
l1 = ['Red','Green','Blue']
l2 = ['Bottle','Chair','Board']

for i in l1:
    for j in l2:
        print(f"{i} - {j}")



