import random
class card:
    FaceValue = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    Suits = ["D", "H", "S", "C"]

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(card.FaceValue[self.value%13]) + card.Suits[self.value//13]

class deck:
    standardDeck = [card(i) for i in range(52)]
    def __init__(self):
        self.cards = deck.standardDeck

    def clear(self):
        self.cards = deck.standardDeck

    def __str__(self):
        string = ''
        for card in self.cards:
            string += str(card) + ' '
        return string

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, n=1):
        cardsDealt = self.cards[:n]
        self.cards = self.cards[n:]
        return cardsDealt

class poker:
    def __init__(self):
        self.cards = deck.standardDeck

# Main
deck1 = deck()
print(deck1)
deck1.shuffle()
print(deck1)
for i in range(5):
    print(deck1.deal()[0])
    print(deck1)
