# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 11:41:26 2018

@author: AMONDI
"""

for value in range(1,5):
    print(value)
    
for value in range(1,20,3):
    print(value)
    
#making a list using range and list functions
even_numbers=list(range(2,30,2))
print(even_numbers)

#squares
squares=[]
for value in range(2,13):
    square=value**2
    squares.append(square)
    print(squares)
    
squares=[]
for value in range(2,13):
    square=value*value
    squares.append(square)
    print(squares)
    
squares=[]
for value in range(10):
    squares.append(value**2)
    print(squares)
 
for i in range(20):
    print('*'*(i+1))
for A in range(11):
    print('A')
    
#list comprehension
squares=[value**2 for value in range(2,11,2)]
print(squares)  

#exercise
for value in range(1,20):
    print(value)
    
for value in range(1,1000000):
    print(value)
    
million=list(range(1,1000000))
print()
    
  
    