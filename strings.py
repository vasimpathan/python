# creating strings
# anything between single or double quote which is collection of character  called string

single_quote_strings = 'Hello'
double_quote_strings = "Hello"
triple_quote_strings = '''Hello'''
print(single_quote_strings)
print(double_quote_strings)
print(triple_quote_strings)

multiline_string = '''
this is line 1 
this is line 2
this is line 3
'''

print(multiline_string)

# accessing char
a =single_quote_strings[0]
print(a)

# Slicing a string
a = single_quote_strings[:4]
print(a)

## to get till 15 char
m= multiline_string[:15]
print(m)

# Negative indexing
l = double_quote_strings[-1]
print(l)

#string concatenation / combine
c = "Hello" + " World"
print(c)

# string Repetition
r = "ha"*3
print(r)

# String length
print(len(single_quote_strings))

# checking substring - nothing but part of the main string
x = "Hello World"
print("Hello" in x) # True
print("hello" in x) # false

# string methods/function
name = "VASIM PATHAN"
print(name.lower())
print(name.upper())
print(name.replace('A','*'))

# f string - used to format the sting
name = "Vasim"
print(f"My name is {name}")


print("Hello is the changes directly added from git hub")
# string operations
print("It's not me")

# multiline string
str = """I am vasim pathan.
I am belong to solapur district.
I am a software developer with 10 years of experience in IT industry"""
print(str)

# String are array
str = "Vasim Pathan"
print(str[1])
print(str[0:5])
print(str[:5])
print(str[-1])
print(str[:-5])

# Concatanation string
s1 = "Vasim"
s2 = "Pathan"
str = s1 + s2
print(str)

# length of string 
print(len(str))

#string cases
str = "vasim"
print(str.lower())
print(str.upper())
print(str.capitalize())

#Replace
str = "Wasim Pathan"
str1 = "Vasim"
print(str.replace("Wasim",str1))

#check string
str = "Vasim pathan Angar"
print("Vasim" in str)

if "Vasim" in str:
  print("Yes present")
else:
  print("Not present")

# looping through a string
str = "Vasim Pathan"
for x in str:
  print(x)
