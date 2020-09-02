from tkinter import *
import random

suits = 'Hearts Spades Diamonds Clubs'.split()
ranks = 'Two Three Four Five Six Seven Eight Nine Ten Jack Queen King Ace'.split()
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
chips = 100


class Card():
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck():
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(rank, suit))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        return "The Deck has " + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


class Hand():
    def __init__(self):
        self.card = []
        self.value = 0
        self.aces = 0

    def addCard(self, card):
        self.card.append(card)
        self.value += values[card.rank]
        if card.rank == 'Ace':
            self.aces += 1

    def adjustAce(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


def makeBet():
    while True:
        try:
            bet_amt = int(input("How many Chips would you like to Bet? "))
        except:
            print("Please provide an integer Input")
        if bet_amt > chips:
            print("Sorry you do not have sufficient chips. You have {} chips".format(chips))
        else:
            break
    return bet_amt


def winBet(bet):
    global chips
    chips = chips + bet
    return chips


def loseBet(bet):
    global chips
    chips -= bet
    return chips


def hit(deck, hand):
    pulled_card = deck.deal()
    hand.addCard(pulled_card)
    hand.adjustAce()


def stand(deck, hand):
    deck_card = deck.deal()
    hand.addCard(deck_card)
    hand.adjustAce


def playerBusts(player, dealer, chips):
    print('Player BUSTED! ')
    loseBet(chips)


def dealerBusts(player, dealer, chips):
    print("Dealer BUSTED! ")
    winBet(chips)


def playerWins(player, dealer, chips):
    print("Player Wins!! ")
    winBet(chips)


def dealerWins(player, dealer, chips):
    print("Dealer Wins ")
    loseBet(chips)


def push(player, dealer):
    print('PUSH,  TIE')


def showsome(player, dealer):
    print("DEALER'S HAND: ")
    print(dealer.card[1])  # , end = " ")
    # print("with value {}". format(dealer.card[1].value))
    print("PLAYER'S HAND:")
    for card in player.card:
        print(card, end=" and ")
    print("with value {}".format(player.value))


def showall(player, dealer):
    print("DEALER'S HAND:")
    for card in dealer.card:
        print(card, end=" and ")
    print("with value {}".format(dealer.value))
    print("PLAYER'S HAND:")
    for card in player.card:
        print(card, end=" and ")
    print("with value {}".format(player.value))


def intro():
    print("Welcome To BlackJack! ")
    print("Get as close to 21 as you can! ")


window = Tk()


if __name__ == '__main__':
    playing = True
    while True:
        deck = Deck()
        deck.shuffle()
        playerHand = Hand()
        playerHand.addCard(deck.deal())
        playerHand.addCard(deck.deal())
        dealerHand = Hand()
        dealerHand.addCard(deck.deal())
        dealerHand.addCard(deck.deal())
        showsome(playerHand, dealerHand)
        bet = makeBet()
        while playing:
            inp = input("Hit(h) or Stand(s) ")
            if inp[0].lower() == 'h':
                hit(deck, playerHand)
                if playerHand.value > 21:
                    playerBusts(playerHand, dealerHand, bet)
                    playing = False

            elif inp[0].lower() == 's':
                playing = False
            else:
                print("Please input h or s only ")
                continue
            break
        if playerHand.value <= 21:
            showsome(playerHand, dealerHand)
            while playing:
                inp = input("Hit(h) or Stand(s) ")
                if inp[0].lower() == 'h':
                    hit(deck, playerHand)
                    if playerHand.value > 21:
                        playerBusts(playerHand, dealerHand, bet)
                        playing = False

                elif inp[0].lower() == 's':
                    playing = False
                else:
                    print("Please input h or s only ")
                    continue
                break
            while dealerHand.value < playerHand.value:
                hit(deck, dealerHand)

            showall(playerHand, dealerHand)

            if dealerHand.value > 21:
                dealerBusts(playerHand, dealerHand, bet)
            elif playerHand.value > dealerHand.value:
                playerWins(playerHand, dealerHand, bet)
            elif playerHand.value < dealerHand.value:
                dealerWins(playerHand, dealerHand, bet)
            else:
                push(playerHand, dealerHand)
        print("Players total chips are {} ".format(chips))

        newgame = input("Would you like to play again? y/n")
        if newgame[0].lower() == 'y':
            playing = True
            continue
        elif newgame[0].lower() == 'n':
            print("Thanks for Playing!")
        break





