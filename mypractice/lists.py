# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 09:21:49 2018

@author: AMONDI
"""
#lists are used to store info
#by asking for index[-1] the last value in the list is returned
counties=['kisumu','nairobi','nakuru','mombasa']
print(counties[2].title())
print(counties[-1])

print("The best tourist destination is "+counties[0].title()+".")

#modifying elements in a list
counties=['kisumu','nairobi','nakuru','mombasa','lamu','kitui']
print(counties)

counties[-2]='kakmega'
print(counties)

#appending elements to a list
counties.append('migori')
print(counties)

#inserting elements to a list
counties.insert(3,'macahakos')
print(counties)

#removing items from a list
#del statement
del counties[4]
print(counties)

#pop() method
popped_counties=counties.pop()
print(counties)
print(popped_counties)

#popping items fro  any position on the list
my_county=counties.pop(2)
print("I love " +my_county.title())

#remove method
counties.remove('kisumu')
print(counties)

too_dry='kitui'
counties.remove(too_dry)
print(too_dry.title()+" is very dry")

#sortinga list permanently
counties.sort()
print(counties)

#sorting a list temporarily
foods=['githeri','samaki','anadazi','cake','juice']
print(foods)
print(sorted(foods))
print(foods)

#printing lists in reverse
foods.reverse()
print(foods)

#finding the length of a list
print(len(counties))
print(len(foods))

    












