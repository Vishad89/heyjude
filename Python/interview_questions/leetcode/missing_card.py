#!/usr/bin/python

# from the deck of cards, find a missing card
# example
# deck = [ [h,1], [s,3], [c,4] ... so on]

def missing_card(deck):
    res = {}
    #total = 91
    for card in deck:
        if card[0] not in res:
            res[card[0]] = []
        res[card[0]].append(card[1])
    
    for k in res:
        res[k] = sum(res[k])
        if res[k] != 91:
            missing_value = 91 - res[k]
            print("missing card is: [%s,%s]" %(k,missing_value))


deck = [["h",1], ["h",2], ["h",3], ["h",4], ["h",5], ["h",6], ["h",7],["h",8],["h",10],["h",11],["h",12],["h",13],["s",1],["s",2],["s",3],["s",4],["s",5],["s",6],["s",7],["s",8],["s",9],["s",10],["s",11],["s",12],["s",13],\
    ["c",1], ["c",2],["c",3],["c",4],["c",5],["c",6],["c",7],["c",8],["c",9],["c",10],["c",11],["c",12],["c",13],["d",1],["d",2],["d",3],["d",4],["d",5],["d",6],["d",7],["d",8],["d",9],["d",10],["d",11],["d",12],["d",13]]
#print(missing_card(deck))
missing_card(deck)
