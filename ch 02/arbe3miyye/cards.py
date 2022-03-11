import random

class Card:
    def __init__(self, suit:str,val:int)->None:
        self.suit=suit
        self.val=val 
    def show(self)-> None:
        print("{} of {}".format(self.val,self.suit))
class Deck:
    def __init__(self)-> None:
        self.cards=[]
        self.build()
    def build(self)->None:
        for suit in ["Spades","clubs","Diamonds",'Hearts']:
            for value in range (1,14):
                self.cards.append(Card(suit,value))
    def show(self)->None:
        for card in self.cards:
            card.show()
    def shuffle(self)->None:
        for index in range(len(self.cards)-1,0,-1):
            randomNumber=random.randint(0,index)
            self.cards[index],self.cards[randomNumber]=self.cards[randomNumber],self.cards[index]
    def drawCard(self)->"Card":
        return self.cards.pop()




class Player:
    def __init__(self, name: str) -> None:
        self.name=name
        self.hand=[]
    def drawFromDeck(self,deck: "Deck"):
        self.hand.append(deck.drawCard())
        return self # why?
    def showHand(self):
        for card in self.hand:
            card.show()

if __name__=="__main__":
    

    deck1=Deck()
    deck1.show()
    deck1.shuffle()
    deck1.show() # cards are shuffled :)

    card=deck1.drawCard()
    print( "---I am drawing a card---")
    card.show()
    player=Player("Chadi")
    player.drawFromDeck(deck1)
    print ("Player chadi has one card now, And it is:")
    player.showHand()