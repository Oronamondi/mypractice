# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 15:56:31 2018

@author: AMONDI
"""

area=(200,400)
print(area[0])

#looping through tuples
foods=('cake','milk','juice','ugali')
for food in foods:
    print(food)
for value in foods:
    print(value)
    
    
#writing over a tuple
print("The original foods were:\n")
for food in foods:
    print(foods)
    
foods=('mursik','sugar','beef')
for food in foods:
    print("The new foods are:\n")
    print(foods)