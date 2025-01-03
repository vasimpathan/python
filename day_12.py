# -*- coding: utf-8 -*-
"""Day_12.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TABGCNF5ZGnwW6y3-3W8poDaxqfCxmz7
"""



"""# **File Handling in Python**"""

# .txt file

# Commented out IPython magic to ensure Python compatibility.
# # prompt: create a txt file here in colab
# 
# %%writefile myfile.txt
# Hello, this is a text file in Colab!
#

# open(filename, mode)

# filename - myfile.txt, myfile.json, ...
# mode - read (r), write (w), append (a), ....

with open('myfile.txt', 'r') as f:
    print(f.read())

with open('myfile.txt', 'a') as f:
    f.write('\nThis is the third line.')

with open('myfile.txt', 'r') as f:
    print(f.read())

# prompt: create a csv file with two cols, two rows

import csv
with open('mycsv.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['col1', 'col2'])
    writer.writerow(['data1', 'data2'])

import pandas as pd

pd.read_csv('mycsv.csv')