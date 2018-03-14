# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 10:34:11 2018

@author: AMONDI
"""
#use of for loop to print invidual elements in a list
players=['susan','jacob','lucy']
for player in players:
    print(player)
    print(player.title()+' is the best'+'!')
    
students=('mary','connie','dave','musa')
for student in students:
    print('Congratulations, '+student.title())
    print("We can't wait to have you in our institution "+student.title()+".\n")
    
#working with part of a list
#looping through a slice
phones=['samsung','huawei','tecno','nokia','motorola',]
for phone in phones[1:3]:
    print(phone)
    
banks=['equity','coop','kcb','stanchart','barclays']
print(banks[2:])

#copying lists
my_books=['red','yellow','black','maroon']
his_books=my_books[:]
print("His books are ")
print(his_books)

