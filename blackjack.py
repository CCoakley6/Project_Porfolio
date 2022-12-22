# This is a blackjack simulator

import random

suits = ("Hearts", "Diamonds", "Spades", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Jack", "Queen", "King", "Ace")
card_values = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7,
               "Eight": 8, "Nine": 9, "Jack": 10, "Queen": 10, "King": 10, "Ace": 11}

playing = True

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        deck_composition = ''
        for card in self.deck:
            deck_composition += '\n ' + card.__str__()
        return "The deck has:" + deck_composition

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        dealt_card = self.deck.pop()
        return dealt_card

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += card_values[card.rank]
        if card.rank == "Ace":
            self.aces += 1

    def check_aces(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

class Chips:
    def __init__(self):
        while True:
            try:
                self.current = int(input("Enter starting chips as integer"))
            except ValueError:
                print("Starting chips must be an integer")
            else:
                if self.current < 0:
                    print("Starting chips must be a positive integer")
                else:
                    break
        self.bet = 0

    def win_bet(self):
        self.current += self.bet

    def lose_bet(self):
        self.current -= self.bet

def make_bet(chips):
    while True:
        try:
            chips.bet = int(input("How many chips would you like to wager?"))
        except ValueError:
            print("Bet must be an integer!")
        else:
            if chips.bet > chips.current:
                print("Bet can't exceed {}".format(chips.current))
            else:
                break

def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.check_aces()

def hit_or_stay(deck,hand):
    global playing

    while True:
        hit_stay = input("\nHit or stay? 'h' for hit, 's' for stay.")

        if hit_stay[0].lower() == 'h':
            hit(deck,hand)

        elif hit_stay[0].lower() == 's':
            print("Play chose to stay.")
            playing = False

        else:
            print("Invalid entry, please try again. 'h' to hit, 's' to stay")
            continue
        break

def show_partial_hands(player, dealer):
    print("\nDealer's Hand")
    print(" [hidden card]")
    print("",dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand Value =", player.value)

def show_all_hands(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand Value =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("PLayer's Hand Value =", player.value)

def player_busts(player, dealer, chips):
    print("\nPlayer busts!")
    chips.lose_bet()

def player_wins(player, dealer, chips):
    print("\nPlayer wins!")
    chips.win_bet()

def dealer_busts(player, dealer, chips):
    print("\nDealer busts")
    chips.win_bet()

def dealer_wins(player, dealer, chips):
    print("\nDealer wins!")
    chips.lose_bet()

def tie():
    print("\nTie! Bet is refunded.")

while True:
    print("Welcome to the casino! Blackjack is the game!\nDealer hits until 17. Aces are 1 or 11.")

    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_chips = Chips()

    make_bet(player_chips)

    show_partial_hands(player_hand, dealer_hand)

    while playing:
        hit_or_stay(deck, player_hand)

        show_partial_hands(player_hand, dealer_hand)

        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            break

    if player_hand.value <= 21:
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        show_all_hands(player_hand, dealer_hand)

        if dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)

        else:
            tie()

    print("\nPlayer's chips are", player_chips.current)

    new_round = input("Do you want to play another round? 'y' or 'n'")

    if new_round[0] == 'y':
        playing = True
        continue
    else:
        print("Game over. Thanks for playing!")
        break



test_deck = Deck()
test_deck.shuffle()
test_player = Hand()
test_player.add_card(test_deck.deal())
test_player.add_card(test_deck.deal())

for card in test_player.hand:
    print(card)
print(test_player.value)