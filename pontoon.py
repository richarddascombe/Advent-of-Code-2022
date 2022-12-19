#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 13:20:35 2022

@author: richard10998
"""
import random
d = {"Jack":10, "Queen":10, "King":10, "Ace":1 , "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9}
deck = []
for i in range(1,14):
    if i == 11:
        card = "Jack"
    elif i == 1:
        card = "Ace"
    elif i == 12:
        card = "Queen"
    elif i == 13:
        card = "King"
    else:
        card = str(i)
    deck.append(card + " hearts")
    deck.append(card + " clubs")
    deck.append(card + " diamonds")
    deck.append(card + " spades")

random.shuffle(deck)

hand1 = []
hand2 = []

no_of_cards = 2
for a in range(no_of_cards):
    hand1.append(deck.pop())
    hand2.append(deck.pop())
print(deck)

print("Player one, your hand is", hand1)
while input("Stick or twist (s or t)?") == "t":
    hand1.append(deck.pop())
    print("Player one, your hand is", hand1)

    hand_value=0
    for c in hand1:
        
        hand_value = hand_value + d.get(c.split()[0])
        if hand_value > 21:
            print("Bust")
            break
           
        
        
    
    

