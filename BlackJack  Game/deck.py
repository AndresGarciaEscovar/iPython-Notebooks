# Random module to shuffle the deck.
import random

# Module to create cards.
import card

class Deck():
    '''
    The class that represents a deck of cards.
    '''
    
    # Constructor
    def __init__(self):
        '''
        Create a deck with 52 distinct cards.
        '''
        # Create a deck with 52 distinct cards.
        self.cards = []
        for i in card.Card.numbers.values():
                for j in card.Card.suits.values():
                    self.cards.append(card.Card(i,j))
    
    # Returns the top card.
    def get_top_card(self):
        '''
        Returns the top card.
        OUTPUT:
            - The top (cards[-1]) card in the deck, unless there are no cards.
        '''
        # Return the top card.
        if(len(self.cards) > 0):
            return self.cards.pop()
        
        # If there are no cards this leads to an error
        return None
    
    # Shuffle the deck.
    def shuffle_deck(self):
        '''
        Shuffles the deck.
        '''
        random.shuffle(self.cards)
