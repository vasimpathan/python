# -*- coding: utf-8 -*-
"""Day_09.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11afTs1w5fKczWtw3pULZYbwvxjsL--Xs
"""

# input, logic, output

print("Hello David!")

"""# **Functions - Basics**

# **1. Defining a Function**
"""

def hello():
  print("Hello world!")

"""# **2. Calling a Function**"""

hello()

# input - inside braces - no
# logic - print
# output - Hello world

"""# **3. Function with Parameters / Params**"""

def hello(name):
  print(f"Hello {name}!")

hello("Rajesh")

"""# **F Strings**"""

country = "Australia"
capital = "Canberra"
print(f"{capital} is the capital city of {country}")

"""# **4. Function with Return value**"""

# two numbers = add them
def add_numbers(x, y):
  return x+y

add_numbers(5, 6)

v = add_numbers(5, 6)

v

"""# **5. Default Params**"""

# def hello(name):
#   print(f"Hello {name}!")

def hello(name="Guest"):
  print(f"Hello {name}!")

hello()

hello("Raju")

"""# **6. Keyword Arguments**"""

# two numbers = add them
def add_numbers(x=10, y=10):
  return x+y

add_numbers()

"""# **7. Scope and Global Variables**"""

def test(x=10):
  print(x)

test(11)

# global var = defined outside the function
x = 100

def test(y):
  global x
  print(x, y)

test(10)

n = 23

def test(n):
  n = 21
  print(n)

test(18)

"""# **8. Nested Functions**"""

def hello(name):
  print(f"Hello {name}")

def fav_city(city_name, name):
  hello(name)
  print(f"Welcome to {city_name}!")

fav_city("Mumbai", "David")