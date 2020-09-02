import random

suits = 'Hearts Spades Diamonds Clubs'.split()
ranks = 'Two Three Four Five Six Seven Eight Nine Ten Jack Queen King Ace'.split()
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


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


class Chips():

    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def winBet(self):
        self.total += self.bet

    def loseBet(self):
        self.total -= self.bet


def makeBet(chips):
    while True:
        try:
            chips.bet = int(input("How many Chips would you like to Bet? "))
        except:
            print("Please provide an integer Input")
        if chips.bet > chips.total:
            print("Sorry you do not have sufficient chips. You have {} chips".format(chips.total))
        else:
            break


def hit(deck, hand):
    singleCard = deck.deal()
    hand.addCard(singleCard)
    hand.adjustAce()


def hitOrStand(deck, hand):
    global playing
    while True:
        x = input("Hit or Stand Press h for Hit and s for Stand ")
        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print("Player Stands, Dealers turn ")
            playing = False
        else:
            print("Please press h or s only")
            continue
        break


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


def playerBusts(player, dealer, chips):
    print("Player Busted, Dealer Wins")
    chips.loseBet()


def dealerBusts(player, dealer, chips):
    print("Dealer Busted, Player Wins")
    chips.winBet()


def playerWins(player, dealer, chips):
    print("Player Wins")
    chips.winBet()


def dealerWins(player, dealer, chips):
    print(" Dealer Wins")
    chips.loseBet()


def push(player, dealer):
    print('TIE, PUSH!')


if __name__  == '__main__':
    playing = True
    print("Welcome to BlackJack!")
    while True:
        deck = Deck()
        deck.shuffle()
        playerHand = Hand()
        playerHand.addCard(deck.deal())
        playerHand.addCard(deck.deal())
        dealerHand = Hand()
        dealerHand.addCard(deck.deal())
        dealerHand.addCard(deck.deal())
        playerChips = Chips()
        showsome(playerHand, dealerHand)
        makeBet(playerChips)
        while playing:
            hitOrStand(deck, playerHand)
            showsome(playerHand, dealerHand)
            if playerHand.value > 21:
                playerBusts(playerHand, dealerHand, playerChips)
            break
        if playerHand.value < 21:
            while dealerHand.value < 17:
                hit(deck, dealerHand)
            showall(playerHand, dealerHand)

            if dealerHand.value > 21:
                dealerBusts(playerHand, dealerHand, playerChips)
            elif playerHand.value > dealerHand.value:
                playerWins(playerHand, dealerHand, playerChips)
            elif playerHand.value < dealerHand.value:
                dealerWins(playerHand, dealerHand, playerChips)
            else:
                push(playerHand, dealerHand)
        print('\n Player total chips are {}'.format(playerChips.total))

        newgame = input("Would you like to play again? y/n")
        if newgame[0].lower() == 'y':
            playing = True
            continue
        elif newgame[0].lower() == 'n':
            print("Thanks for Playing!")
        break

