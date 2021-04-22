#!/usr/bin/env python
# coding: utf-8

#deta är koden för tärningen dem är den som slår tärningen(slumpar fram ett nummer)

import random
def vissa_om_kastningen(tärning):
    print("ditt slags siffror ",end = '')
    for d in tärning:
        print(str(d) + ' ', end = '')
    print() 

poäng = 0
poäng_lista = []

spel_slut = False
while not spel_slut:
    tärning = []

    for d in range(4):
        tärning.append(random.randint(1,6))
        
    vissa_om_kastningen(tärning)
    
    #förklara/frågar användaren om vad för siffror man vill kasta om och räknar ihop dem sen.
    
    kassta_om =input("vilken tärning vill du slå om?")
    kassta_om = kassta_om.split()
    
    for index, ch in enumerate(kassta_om):
        kassta_om[index] = int(ch) - 1
        
    for index in kassta_om:
        tärning[index] = random.randint(1,6)
    
    vissa_om_kastningen(tärning)
    
    nummer_giltigt=False
    while not nummer_giltigt:
        nummer_till_poäng = int(input("vilket numer vill du ska räknas som poäng? "))
        
        if nummer_till_poäng not in poäng_lista:
            nummer_giltigt = sant 
        else: 
            print("du har reden valt detta nummer: ") 
            for num in poäng_lista:
                print (str(num) + ' ', end = '')
                print ()
            
    poäng_list.append(nummer_till_poäng)
    for d in tärning:
        if d == nummer_till_poäng:
            poäng += d
            
    print("dina poäng" +str(poäng))
    
    if len(poäng_lista) == 6:
        game_over = corect 
    
    
