import random
class cards:
    number = ['A', 'K', 'Q', 'J', '10', '9', '8', '7','6', '5', '4', '3', '2']
    suits = ['-h', '-s', '-c', '-d']
    deck = []
    def __init__(self):
        for card in self.number:  
            for suit in self.suits:  
                self.deck.append(card + suit )  

    def shuffle(self):
        pass


class player:
    def __init__(self, name: str, cards: list, chips: int):
        self.name = name
        self.cards = cards
        self.chips = chips
        self.pos = ''
        self.paid_round = 0
        self.playerType = 'default'

    def action(self, community_cards = None,):
        if(toCall == bigBlind):
            actions = ["check", "bet", "raise", "fold"]
            choice = random.randint(0, len(actions))
            if(actions[choice] != "check" and actions[choice] != "fold" ):
                #bet
                bet_size = random.randint(bigBlind*2, self.chips)
                return actions[choice],  bet_size
            elif(actions[choice] == "check" or actions[choice] == "fold"):
                return  actions[choice], 0
        else:
            actions = ["raise", "fold"]
            choice = random.randint(0, len(actions))
            if(actions[choice] == "raise"):
                #raise 2 times the previous raiser
                bet_size = random.randint(toCall * 2, self.chips)
                return actions[choice], bet_size
            else:
                #fold
                return actions[choice], 0




    
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
    





card  = cards()



p2 = player('bot-1', ['J-h','J-d'],1000)
p3 = player('bot-2', ['A-h', 'A-d'], 1000)
p4 = player('bot-3', [], 1000)
p5 = player('bot-4', [], 1000)
p6 = player('bot-5', [], 1000)
p1 = player('player', [], 1000)


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

#while playing:
 #   def assign_pos(p1, p2, p3)
    #pay_blinds()
     
    #under the gun action 
                #blinds # bet   #call # sb raise bb call d re raise 
    
smallBlind = 5
bigBlind = 10
Pot = 0
toCall = bigBlind
#actions = ["check", "bet", "raise", "fold"]
last_player = players[2].name


def pre_flop_action(players_queue):
    '''
    pre flop loop goes here 
    '''
    #pay blinds()
    for i, p in enumerate(players):
        if(p.pos == "SB"):
            p.chips -= smallBlind
            p.paid_round += smallBlind
        if(p.pos == "BB"):
            p.chips -= bigBlind
            p.paid_round += bigBlind

    while(roundFlag):
        p = players_queue.get()
        action, bet_size = p.action()
        if(action == "fold"):
            #reset player?
            continue

        elif(action == "bet" or action == "raise")
    #check action 
    #p.set_paid_round()                

    # add player  to end of the Q
    players_queue.put(p)

    #check if paid is equal
    #True, False function()
    
    
    #pay 20  to call = max - pay = 80
    #pay 50  to call 50     paid hame barabar bood
    #pay 100  
