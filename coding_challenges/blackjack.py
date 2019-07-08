import json
import random
from flask import Flask, request
app = Flask(__name__)


"""
BlackJack API in Python

- /game Starts a Blackjack Game
- /hand User receives hand as well as the dealer hand
- /hit Add a random card from the deck to player hand
- /stay Stay at current state, wait for dealer to make next move

- Card
- Hand
- Game
- Deck (todo)
"""

class Card:
    def __init__(self, suite, name, value):
        self.suite = suite
        self.name = name
        self.value = value

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def is_blackjack(self): # bool
        count = 0
        for card in self.cards:
            count += card.value
        return count == 21

    def bust(self):
        count = 0
        for card in self.cards:
            count += card.value
        return count > 21

    def toDict(self):
        # return state of a hand as a dict so that it can be
        # serialized to JSON
        return {
            "cards": [
                {
                    "suite": card.suite,
                    "name": card.name,
                    "value": card.value
                } for card in self.cards
            ]
        }

class Game:
    def __init__(self):
        self.deck = []
        self.dealer_hand = Hand()
        self.user_hand = Hand()
        self.is_started = False

    def play(self):
        self._init_deck()
        for _ in range(2):
            self.dealer_hand.add_card(self.deck.pop())
        for _ in range(2):
            self.user_hand.add_card(self.deck.pop())

    def _init_deck(self):
        new_deck = []
        suites = ["spade", "heart", "clubs", "diamonds"]
        cardname_to_value = {
            'A': 1,
            '2': 2,
            '3': 3,
            '4': 4,
            '5': 5,
            '6': 6,
            '7': 7,
            '8': 8,
            '9': 9,
            '10': 10,
            'J': 10,
            'Q': 10,
            'K': 10,
        }

        for suite in suites:
            for name, value in cardname_to_value.items():
                new_deck.append(Card(suite, name, value))
        self.deck = new_deck

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def user_hit(self):
        self.user_hand.add_card(self.deck.pop())

    def dealer_hit(self):
        self.dealer_hand.add_card(self.deck.pop())

    def get_state(self):
        if self.user_hand.is_blackjack():
            return "Blackjack you win!"
        if self.user_hand.bust():
            return "Bust! dealer wins"
        if self.dealer_hand.bust():
            return "Dealer busts!! you win!"

        current_hand = {
            "your_hand": self.user_hand.toDict(),
            "dealer_hand": self.dealer_hand.toDict(),
        }
        return json.dumps(current_hand)



GAME = Game()

# routes
@app.route('/game')
def game():
    GAME.play()
    return "Game initialized!!!!"

@app.route('/hand')
def hand():
    GAME.play()
    return GAME.get_state()

@app.route('/hit')
def hit():
    GAME.user_hit()
    return GAME.get_state()

@app.route('/check')
def check():
    GAME.dealer_hit()
    return GAME.get_state()
