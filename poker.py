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

    def action(self):
        pass
    
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
    





c1 = cards()
p1 = player('ali', ['A-h', 'A-d'], 200)

p2 = player('hoss', ['J-h','J-d'],100)
p3 = player('player', [], 1000)
p4 = player('HH', [], 2000)

players = [p1, p2, p3, p4]
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

from queue import Queue
players_queue = Queue(max_size = 0)
players_queue.put(players[3]) 
players_queue.put(players[0])
players_queue.put(players[1])
players_queue.put(players[2])

#while playing:
 #   def assign_pos(p1, p2, p3)
    #pay_blinds()
     
    #under the gun action 
                #blinds # bet   #call # sb raise bb call d re raise 
    

def pre_flop_action(players_queue):
    '''
    pre flop loop goes here 
    '''
    p = players_queue.get() 
    action, amount_to_call = p.action(preact='') 
    #check action 
    #p.set_paid_round()                

    # add player  to end of the Q
    players_queue.put(p)

    #check if paid is equal
    #True, False function()
    
    
    #pay 20  to call = max - pay = 80
    #pay 50  to call 50     paid hame barabar bood
    #pay 100  
