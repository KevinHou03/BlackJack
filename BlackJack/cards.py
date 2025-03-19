# Define a card
import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value}{self.suit}"


# Define a set of cards (52 cards without jokers)
class Cards:

    suits = ['♠', '♥', '♣', '♦']
    values = [str(i) for i in range(2, 11)] + ['J', 'Q', 'K', 'A']

    def __init__(self, num_decks=1):
        self.num_decks = num_decks
        self.reset()

    def shuffle(self):
        random.shuffle(self.cards)

    def reset(self):
        self.cards = [
            Card(suit, value)
            for _ in range(self.num_decks)  # 生成 num_decks 副牌
            for suit in self.suits
            for value in self.values
        ]
        self.shuffle()
    #抽牌
    def deal_card(self):
        if len(self.cards) == 0:
            raise ValueError("No cards to draw")
        return self.cards.pop()




# test
# test_cards = Cards()
# print(f"The deck is {test_cards.cards}\nThere are totally {len(test_cards.cards)} cards in the deck)")