# Simple blackjack game in Python

import random

# Initialize suits, ranks, and values of ranks
suits = ['Hearts', 'Clubs', 'Diamonds', 'Spades']
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Jack', 'Queen', 'King', 'Ace']
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


playing = True

# Create card class
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit

# Create deck class
class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_composition = ''
        for card in self.deck:
            deck_composition += '\n' + card.__str__()
        return "The deck contains:" + deck_composition

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card

# Create hand class
class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace'
            self.aces += 1

    def adjust_for_ace(self):
        while self.values > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

# Create Chip class
class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet

# Function to take a bet
def make_bet(chips):
    while True:
        try:
            chips.bet = int(input("How much would you like to wager?"))
        except ValueError:
            print("Wager must be an integer")
        else:
            if chips.bet > chips.total:
                print("Bet cannot exceed", chips.total)
            else:
                break

# Functions to display cards
def show_partial(player, dealer):
    print("\nDealer's Hand")
    print("[hidden card]")
    print('', dealer.cards[1])
    print("\nPlayer's Hand: ", *player.cards, sep='\n')
    print("Player's Hand Value:", player.value)

def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep="\n")
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand: ", *player.cards, sep= '\n')
    print("Player's Hand Value:", player.value)

# Functions for win-loss scenarios
def player_busts(player, dealer, chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print("Dealer busts!")
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print("Dealer wins!")
    chips.lose_bet()

def tie(player, dealer):
    print("It's a tie! Bets are returned.")

# Game logic flow
print("Welcome to Collin's Casino! The game is Blackjack\nThe dealer hits until 17. Aces are 1 or 11.")
player_chips = Chips()
print("Players start ouf with 100 chips.")

while True:
    # Create deck, shuffle, and deal 2 cards to player and dealer
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    # Player places a bet
    make_bet(player_chips)

    show_partial(player_hand, dealer_hand)

    # While loop depending on hitting or staying
    while playing:





