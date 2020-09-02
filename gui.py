from tkinter import *
import random
from time import sleep

suits = 'Hearts Spades Diamonds Clubs'.split()
ranks = 'Two Three Four Five Six Seven Eight Nine Ten Jack Queen King Ace'.split()
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10,
          'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
chips = 100
placeBet = False
bet = 0
si = 1
sj = 1
cardImg = {"Two of Hearts":"2h.gif", "Three of Hearts": "3h.gif", "Four of Hearts":"4h.gif", "Five of Hearts":"5h.gif",
"Six of Hearts":"6h.gif", "Seven of Hearts":"7h.gif","Eight of Hearts":"8h.gif","Nine of Hearts":"9h.gif","Ten of Hearts":"10h.gif",
"Jack of Hearts":"jh.gif","Queen of Hearts":"qh.gif","King of Hearts":"kh.gif","Ace of Hearts":"ah.gif",

"Two of Clubs":"2c.gif","Three of Clubs": "3c.gif","Four of Clubs":"4c.gif", "Five of Clubs":"5c.gif",
"Six of Clubs":"6c.gif", "Seven of Clubs":"7c.gif","Eight of Clubs":"8c.gif","Nine of Clubs":"9c.gif","Ten of Clubs":"10c.gif",
"Jack of Clubs":"jc.gif","Queen of Clubs":"qc.gif","King of Clubs":"kc.gif","Ace of Clubs":"ac.gif",

"Two of Diamonds":"2d.gif", "Three of Diamonds": "3d.gif","Four of Diamonds":"4d.gif", "Five of Diamonds":"5d.gif",
"Six of Diamonds":"6d.gif", "Seven of Diamonds":"7d.gif","Eight of Diamonds":"8d.gif","Nine of Diamonds":"9d.gif",
"Ten of Diamonds":"10d.gif","Jack of Diamonds":"jd.gif","Queen of Diamonds":"qd.gif","King of Diamonds":"kd.gif","Ace of Diamonds":"ad.gif",

"Two of Spades":"2s.gif","Three of Spades": "3s.gif","Four of Spades":"4s.gif", "Five of Spades":"5s.gif",
"Six of Spades":"6s.gif", "Seven of Spades":"7s.gif","Eight of Spades":"8s.gif","Nine of Spades":"9s.gif","Ten of Spades":"10s.gif",
"Jack of Spades":"js.gif","Queen of Spades":"qs.gif","King of Spades":"ks.gif","Ace of Spades":"as.gif"}

playerHand = []
dealerHand = []
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

    def __len__(self):
        return len(self.card)


def makeBet():
    global chips
    global placeBet
    global bet
    bet = int(bet_val.get())
    if bet > chips:
        sm = "Sorry you do not have suffiecient chips. You have " + str(chips) + " chips"
        bet_info.delete("1.0", END)
        bet_info.insert(END, sm)
        placeBet = False
    else:
        s = "You bet " + str(bet) +". You have "+ str(chips - bet) + " remaining"
        bet_info.delete("1.0", END)
        bet_info.insert(END, s)
        placeBet = True

def hit(deck, hand):
    playing = True
    global betamt
    pulled_card = deck.deal()
    hand.addCard(pulled_card)
    hand.adjustAce()

def playerhit():
    playing = True
    global deck
    global playerHand
    global dealerHand
    global betamt
    playerHand.addCard(deck.deal())
    playerHand.adjustAce()
    showsome(playerHand, dealerHand)
    if playerHand.value >21:
        playerBusts(playerHand, dealerHand, betamt)
        hitBtn['state'] = 'disabled'
        betBtn['state'] = 'normal'
        standBtn['state'] = 'disabled'

def stand():
    global betamt
    global playerHand
    global dealerHand
    betBtn['state'] = 'normal'
    hitBtn['state'] = 'disabled'
    standBtn['state'] = 'disabled'
    showall(playerHand, dealerHand)

    if playerHand.value > 21:
        playerBusts(playerHand, dealerHand, betamt)

    elif playerHand.value <=21:
        while dealerHand.value < 17:
            hit(deck, dealerHand)

        showall(playerHand, dealerHand)

        if dealerHand.value >21:
            dealerBusts(playerHand, dealerHand, betamt)
        elif playerHand.value > dealerHand.value:
            playerWins(playerHand,dealerHand, betamt)
        elif playerHand.value < dealerHand.value:
            dealerWins(playerHand, dealerHand, betamt)
        else:
            push(playerHand, dealerHand)


def winBet(bet):
    global chips
    chips = chips + bet
    return chips


def loseBet(bet):
    global chips
    chips -= bet
    return chips


def showsome(player, dealer):
    global si
    global sj
    global playerHand
    global pi
    global pci
    pci = []
    pi = []
    pcl = []
    k = 0
    global dci
    dc = dealer.card[0]
    dci = PhotoImage(file = cardImg[str(dc)])
    dcards.delete("1.0", END)
    dcards.image_create(END, image = dci)
    #print(cardImg[str(dc)])
    #dcl = Label(window, image = dci)
    #dcl.grid(row = 1, column = 1)
    #dcards.delete("1.0", END)
    #dcards.insert(END, dc)
    #pcards.delete("1.0", END)

    for card in player.card:
        pci.append(card)
    for i in range(len(pci)):
        pi.append(PhotoImage(file = cardImg[str(pci[i])]))

        #pcl.append(Label(window, image = pi[i]))
        #pcl[k].grid(row = 2, column = i+1)
        #k = k+1
        pcards.image_create(END,image = pi[i])
    #print(pi)
    #window.mainloop()



def showall(player, dealer):
    global window
    dcards.delete("1.0", END)
    pcards.delete("1.0", END)
    global di
    global psi
    dcsi = []
    pcsi = []
    di = []
    psi = []
    for card in dealer.card:
        dcsi.append(card)
    for i in range(len(dcsi)):
        di.append(PhotoImage(file=cardImg[str(dcsi[i])]))
        #dl.append(Label(window, image = di[i]))
        #dl[m].grid(row = 1, column = i+1)
        #m = m+1
        dcards.image_create(END, image = di[i])
    for card in player.card:
        pcsi.append(card)
    for i in range(len(psi)):
        psi.append(PhotoImage(file=cardImg[str(pcsi[i])]))
        #pl.append(Label(window, image=psi[i]))
        #pl[k].grid(row=2, column=i + 1)
        #k = k + 1
        pcards.image_create(END, image = psi[i])



def playerBusts(player, dealer, beta):
    global chips
    global betamt
    gs_text.delete("1.0", END)
    gst = "Player Busted Dealer Wins"
    gs_text.insert(END, gst)
    loseBet(beta)
    hs_text.delete("1.0", END)
    cl = "You have " + str(chips) + " remaining"
    hs_text.insert(END, cl)



def dealerBusts(player, dealer, beta):
    global chips
    global betamt
    gs_text.delete("1.0", END)
    gst = "Dealer Busted Player Wins"
    gs_text.insert(END, gst)
    winBet(beta)
    hs_text.delete("1.0", END)
    cl = "You have " + str(chips) + " remaining"
    hs_text.insert(END, cl)



def playerWins(player, dealer, beta):
    global chips
    global betamt
    gs_text.delete("1.0", END)
    gst = "Player Wins"
    gs_text.insert(END, gst)
    winBet(beta)
    hs_text.delete("1.0", END)
    cl = "You have " + str(chips) + " remaining"
    hs_text.insert(END, cl)


def dealerWins(player, dealer, beta):
    global chips
    global betamt
    gs_text.delete("1.0", END)
    gst = "Dealer Wins"
    gs_text.insert(END, gst)
    loseBet(beta)
    hs_text.delete("1.0", END)
    cl = "You have " + str(chips) + " remaining"
    hs_text.insert(END, cl)



def push(player, dealer):
    gs_text.delete("1.0", END)
    gst = "PUSH, TIE"
    gs_text.insert(END, gst)
    hs_text.delete("1.0", END)
    cl = "You have " + str(chips) + " remaining"
    hs_text.insert(END, cl)




def gamestart():
    hitBtn['state'] = 'disabled'
    betBtn['state'] = 'normal'
    dcards.delete("1.0", END)
    pcards.delete("1.0", END)
    gs_text.delete("1.0", END)
    #bet_info.delete("1.0", END)
    hs_text.delete("1.0", END)
    bet_info.delete("1.0", END)


def gameplay():
    global deck
    global playerHand
    global dealerHand
    global betamt
    gamestart()
    hitBtn['state'] = 'normal'
    betBtn['state'] = 'disabled'
    standBtn['state'] = 'normal'
    deck = Deck()
    deck.shuffle()
    playerHand = Hand()
    playerHand.addCard(deck.deal())
    playerHand.addCard(deck.deal())
    dealerHand = Hand()
    dealerHand.addCard(deck.deal())
    dealerHand.addCard(deck.deal())
    showsome(playerHand, dealerHand)
    betamt = bet
    if playerHand.value == 21:
        playerWins(playerHand, dealerHand, betamt)


window = Tk()
window.title("BlackJack")
l1 = Label(window, text="Welcome to BlackJack!\n"
                        "NOTE: You start with 100 chips")
l1.grid(row=0, column=0, columnspan=3)

dhand = Label(window, text="Dealer's Hand: ")
dhand.grid(row=1, column=0)
dcards = Text(window, height=5, width=60)
dcards.grid(row=1, column=2)

phand = Label(window, text="Player's Hand: ")
phand.grid(row=2, column=0)
pcards = Text(window, height=5, width=60)
pcards.grid(row=2, column=2)

bl = Label(window, text="Input Bet in Integer")
bl.grid(row=3, column=0)
bet_val = StringVar()
bet_entry = Entry(window, textvariable=bet_val)
bet_entry.grid(row=3, column=2)

betl = Label(window, text="Bet Status")
betl.grid(row=4, column=0)
bet_info = Text(window, height=1, width=60)
bet_info.grid(row=4, column=2)
betBtn = Button(window, text="Place Bet", command=makeBet)
betBtn.grid(row=3, column=3)

hsl = Label(window, text="Hit(h) or Stand (s)")
hsl.grid(row=5, column=0)
dealBtn = Button(window, text = "Deal", command = gameplay)
dealBtn.grid(row = 5, column = 2)
hitBtn = Button(window, text="Hit", command=playerhit)
hitBtn.grid(row=5, column=3)
standBtn = Button(window, text="Stand", command = stand)
standBtn.grid(row=5, column=4)
hs_text = Text(window, height=1, width=40)
hs_text.grid(row=6, column=2)
playagainbtn = Button(window, text = "Play Again", command = gamestart)
playagainbtn.grid(row = 9, column = 0)
gl = Label(window, text="Game Status")
gl.grid(row=8, column=0)

gs_text = Text(window, height=1, width=40)
gs_text.grid(row=8, column=2)

window.mainloop()
