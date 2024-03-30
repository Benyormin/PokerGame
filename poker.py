import random
class Cards:
    number = ['A', 'K', 'Q', 'J', '10', '9', '8', '7','6', '5', '4', '3', '2']
    suits = ['♥', '♠', '♣', '♦']
    #♣♠♦♥
    deck = []
    def __init__(self):
        for c in self.number:
            for suit in self.suits:  
                self.deck.append(c + suit )





class Player:
    def __init__(self, name: str, cards: list, chips: int):
        self.name = name
        self.cards = cards
        self.chips = chips
        self.pos = ''
        self.paid_round = 0
        self.playerType = 'default'

    def action(self, community_cards = None,):

        if(toCall == bigBlind):
            actions = ["check", "bet", "raise", "fold", "call"]
            choice = random.randint(0, len(actions)-1)
            if (actions[choice] == "call"):
                return actions[choice], toCall
            if(actions[choice] != "check" and actions[choice] != "fold" ):
                #bet
                bet_size = random.randint(bigBlind*2, self.chips)
                return actions[choice],  bet_size
            elif(actions[choice] == "check" or actions[choice] == "fold"):
                return  actions[choice], 0
        else:
            #raised before
            actions = ["raise", "fold", "call"]
            choice = random.randint(0, len(actions)-1)
            if (actions[choice] == "call"):
                return actions[choice], toCall
            if(actions[choice] == "raise"):
                #raise 2 times the previous raiser
                bet_size = random.randint(toCall * 2, self.chips)
                return actions[choice], bet_size
            else:
                #fold
                return actions[choice], 0




    #TODO: add draw function
    def hand_strength(self):
        pass

    def set_position(self, position):
        #sb, BB, D , ...
        self.pos = position
    
    def set_paid_round(self, amount):
        self.paid_round = amount


    def get_paid_round(self):
        return self.paid_round
    

    def toString(self):
         print(f' name: {self.name} \n cards: {self.cards} \n chips: {self.chips}$')



def assign_pos(players):
    players[0].set_position('D')
    players[1].set_position('SB')
    players[2].set_position('BB')
    









p2 = Player('bot-1', [],1000)
p3 = Player('bot-2', [], 1000)
p4 = Player('bot-3', [], 1000)
p5 = Player('bot-4', [], 1000)
p6 = Player('bot-5', [], 1000)
p1 = Player('player', [], 1000)


players = [p1, p2, p3, p4, p5, p6]
playing = True
#generate random number for dealer
random.shuffle(players)
#for idx, data in enumerate(players):
 #   print(data.toString())
#assign_pos(players)

players[0].set_position('D')
players[1].set_position('SB')
players[2].set_position('BB')
players[3].set_position('UDG')
players[4].set_position('+1')
players[5].set_position('CO')

from queue import Queue
players_queue = Queue()
players_queue.put(players[3]) 
players_queue.put(players[4])
players_queue.put(players[5])
players_queue.put(players[0])
players_queue.put(players[1])
players_queue.put(players[2])


card  = Cards()
deck = card.deck
random.shuffle(deck)
print(deck)
print(deck.pop(0))
print(deck.pop(0))
print(deck)
smallBlind = 5
bigBlind = 10
Pot = 0
toCall = bigBlind
#actions = ["check", "bet", "raise", "fold"]
last_player = players[2].name  # bigblind last player to act
firstTimeFlag = True


def pre_flop_action(toCall= toCall, players_queue= players_queue, firstTimeFlag= firstTimeFlag, last_player = last_player):

    #pay blinds()


    for i, p in enumerate(players):
        if(p.pos == "SB"):
            p.chips -= smallBlind
            p.set_paid_round(smallBlind)
        if(p.pos == "BB"):
            p.chips -= bigBlind
            p.set_paid_round(bigBlind)

    while(True):

        p = players_queue.get()
        if (last_player == p.name and (not firstTimeFlag)) :
            # end the round
            print("round is over ..")
            break
        action, bet_size = p.action()
        if(firstTimeFlag):
            firstTimeFlag = False

        if(action == "fold"):
            #reset player?()
            continue

        elif(action == "bet" or action == "raise"):
            p.chips -= bet_size
            p.set_paid_round(bet_size)
            toCall = bet_size
            players_queue.put(p)
            last_player = p.name

        elif(action == "call"):
            p.chips -= toCall
            p.set_paid_round(toCall)
            players_queue.put(p)

    #check action 
    #p.set_paid_round()                

    # add player  to end of the Q


    #check if paid is equal
    #True, False function()
    
    
    #pay 20  to call = max - pay = 80
    #pay 50  to call 50     paid hame barabar bood
    #pay 100
pre_flop_action(toCall, players_queue, firstTimeFlag, last_player)


