# -*- coding: utf-8 -*-
"""
Created on Tue Apr  5 01:15:36 2022

@author: DELL
"""

simpleLogin = {
    1: {"firstname": "Nathan", "lastname": "Moore", "email address": "nmoore12@gmail.com", "password": "qwerty1",},
    #2: {"firstname": "Kate", "lastname": "Cooper", "email address": "kcooper63@gmail.com", "password": "saved4it",}, 
    #3: {"firstname": "Emmanuel", "lastname": "Johnson", "email address": "ejohnson4@gmail.com", "password": "Money4me",},
    }

email = input("enter email address: ")
passw = input("enter password: ")
#value = simpleLogin[1]

for users, value in simpleLogin.items():
    if (email == value["email address"] and passw == value["password"]):
        print ("hello ", value["firstname"], value["lastname"], " you have succefully logged in")
    else:
        while email != value["email address"] and  passw != value["password"] :
            print("Wrong combination of email and/or password. Try again!.")
            email = input("enter email address: ")
            passw = input("enter password: ")
            if (email == value["email address"] and passw == value["password"]):
              print ("hello ", value["firstname"], value["lastname"], " you have succefully logged in")
            else:
                print()
        
        
        