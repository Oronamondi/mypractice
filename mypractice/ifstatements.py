# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 17:41:18 2018

@author: AMONDI
"""

alien_color='green'
if alien_color=='green':
    print("The player just earned 5 points")
    
alien_colors=['green','yellow','red']
for alien_color in alien_colors:
    if alien_color=='yellow':
        print("The player just earned 5 points")
        
alien_colors=['green','yellow','red']
if 'green' in alien_colors:
   print("The player just earned 5 points") 

alien_colors=['green','yellow','red']
if 'blue' not in alien_colors:
   print("The player just lost 5 points")

alien_color='red'
if (alien_color == 'red') or (alien_color=='blue'):        
    print("The player just earned 5 points")
    
    
alien_color='red'
if (alien_color == 'red') and (alien_color=='blue'):        
    print("The player just earne 5 points")

users=['admin','levi','keith','eric']
for user in users:
    if user=='admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello, "+user.title()+ " thank you for logging in again" +".")
        
        
users=[]
if users:
    for user in users:
        print("Hello, "+users.title()+"thank you for logging in again"+".")
    else:
        print("We need to find some users"+"!")
        
current_users=['levi','keith','eric','liz','perry']
new_users=['liz','derick','jake','keith','john']
for new_user in new_users:
    if new_user in current_users:
        print(new_user+" has already been used, enter another username"+".")
    else:
        print(new_user+" is available"+".")
        
numbers=list(range(1,10))
for number in numbers:
    if number==1:
        print( str(number) + "st")
    elif number==2:
        print(str(number)+"nd")
    elif number==3:
        print(str(number)+"rd")
    else:
        print(str(number)+"th")
        