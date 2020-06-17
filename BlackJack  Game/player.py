# Module to import cards.
import card

class Player():
    '''
    The class that represents a player of the game.
    '''
    
    # Constructor
    def __init__(self, money = 50000):
        '''
        Constructs a player.
        INPUT:
            - money: The initial amount of money the player has; has a value of 50000 by default.
        '''
        self.money = int(money)
        self.cards = []
        self.cardVals = []
        
    # Place a bet, if possible.
    def place_bet(self, bet):
        '''
        Takes the bet amount from the player, if the player has enough money.
        INPUT:
            - bet: The amount of money the player wants to bet.
        OUTPUT:
            - The bet money if the player has enough money, otherwise returns None.
        '''
        # Player puts money down
        if (self.money - bet) >= 0:
            self.money -= bet
            return bet
        else:
            return None
    
    # Receives a card.
    def receive_card(self, crd, idx):
        '''
        Receives the value of the card that the player gets possesses.
        INPUT: 
            - crd: The card that the player receives.
            - idx: The index where the value of the card is located.
        '''
        self.cards.append(crd)
        self.cardVals.append(crd.number[idx])
    
    # Receive money from a bet.
    def receive_money(self, received):
        '''
        The amount of money a player receives.
        INPUT:
            - The amount of money the player receives from the bet.
        '''
        self.money += received
    
    # Returns all the cards the player has.
    def return_cards(self):
        '''
        Returns the cards the player has.
        OUTPUT: 
            - The cards (Card[])that the player has.
        '''
        return self.cards
    
    # The sum of the cards.
    def return_cards_sum(self):
        '''
        Returns the sum of the cards the player has.
        OUTPUT:
            - The sum (int) of the cards the player has.
        '''
        return sum(self.cardVals)
