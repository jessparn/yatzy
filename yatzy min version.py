#!/usr/bin/env python
# coding: utf-8

#deta är koden för tärningen dem är den som slår tärningen(slumpar fram ett nummer)

import random
def vissa_om_kastningen(tärning):
    print("deta är tärnings siffrorna",end = '')
    for d in tärning:
        print(str(d) + ' ', end = '')
    print() 
regler = ("användaren ska starta programet och dåkommer programtet att slå en tärning(slumpar fram ett nummer) och användaren kommer få välja vilka sifror som personen vill kasta om, när personen har valt : ")
poäng=0
tärning = []

print(regler)

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

numer_till_poäng = int(input("vilket numer vill du ska räknas som poäng? "))
poäng_list.append(numer_till_poäng)
for d in tärning:
    if d == numer_till_poäng:
        poäng += d
print("dina poäng" +str(poäng))


