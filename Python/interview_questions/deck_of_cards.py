
## SHUFFLING A DECK OF CARDS
## A deck of cards has 13 cards each of 4 suits: heart(♥), spade(♠), diamond(♦), club(♣).
## THOUGHT PROCESS: Construct an unshuffled deck by using two lists, one for suits, another for cardValues 
## Shuffle the deck by iterating over all cards one by one using their indexes, and swapping the index with any random index.

import random
import itertools

def deck_crete():
    suits = [ "Hearts", "Spade", "Diamond" , "Club" ]
    faces = list(range(2,11))
    faces.extend(["Jack", "Queen", "King"])
    faces.insert(0,"Ace")
    suits = ['Spade', 'Heart', 'Diamond', 'Club']
    deck = list(itertools.product(faces, suits))
    deck = shuffleDeck(deck)
    draw_card(deck)

def shuffleDeck(deck):
    for i, card in enumerate(deck):
        insert_at = random.randrange(52)
        deck[i], deck[insert_at] = deck[insert_at], deck[i]
    return deck

def draw_card(deck):
    t = int(input("How many cards are we drawing? : "))
    print("//// You Hand ///")
    for r in range(t):
        r = random.choice(deck)
        print("{0[0]} of {0[1]}" .format(r))

deck_crete()