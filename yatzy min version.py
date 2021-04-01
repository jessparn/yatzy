#!/usr/bin/env python
# coding: utf-8

import random
def vissa_om_kastningen(tärning):
    print("deta är tärnings siffrorna",end = '')
    for d in tärning:
        print(str(d) + ' ', end = '')
    print() 
    
poäng=0
tärning = []

for d in range(4):
    tärning.append(random.randint(1,6))
    
vissa_om_kastningen(tärning)

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


