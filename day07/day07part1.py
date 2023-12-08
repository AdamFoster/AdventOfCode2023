#answer = 251106089
#250531843 is too low
#250539501 is too low

from dataclasses import dataclass
from collections import Counter

#filename = 'sample01.txt'
filename = 'input.txt'

@dataclass
class Hand:
    cards: []
    bid: int
    rank: int
    typ: int

    def __lt__(self, other):
        if self.typ == other.typ:
            for a,b in zip(self.cards, other.cards):
                if a != b:
                    return a < b
            return False
            #return self.cards < other.cards
        return self.typ < other.typ
    def __eq__(self, other):
        if self.typ == other.typ:
            return self.cards == other.cards
        return False

hands = []
with open(filename, "r") as f:
    for line in f:
        cards, bid = line.split()
        cardsvalues = []
        for c in cards:
            if c.isdigit():
                cardsvalues.append(int(c))
            else:
                if c == "T":
                    cardsvalues.append(10)
                elif c == "J":
                    cardsvalues.append(11)
                elif c == "Q":
                    cardsvalues.append(12)
                elif c == "K":
                    cardsvalues.append(13)
                elif c == "A":
                    cardsvalues.append(14)
        counts = Counter(cardsvalues)
        typ = -1
        if len(counts) == 5:
            typ = 0
        elif len(counts) == 4:
            typ = 1
        elif len(counts) == 3:
            v = list(counts.values())
            if v[0] == 2 or v[1] == 2 or v[2] == 2:
                typ = 2 #2 pair
            else:
                typ = 3 #3 of a kind
        elif len(counts) == 2:
            v = list(counts.values())
            if v[0] == 3 or v[1] == 3:
                typ = 4 #full house
            else:
                typ = 5 #4 of a kind
        else:
            typ = 6 #5 of a kind
        hands.append(Hand(cardsvalues, int(bid), -1, typ))
#print(hands)
#print()
hands.sort()
#hands.reverse()


total = 0
for i, h in enumerate(hands):
    h.rank = i+1
    total += h.rank * h.bid
    print(h)
#print(hands)
print(total)