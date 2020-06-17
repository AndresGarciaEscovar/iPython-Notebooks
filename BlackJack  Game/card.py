# Class that represents a card.

class Card():
    '''
    The class that represents a card.
    '''
    
    # Dictionary of possible cards and their possible in-game value.
    numbers = {
        'Ace': (1, 11,'A'),
        '2': (2, 2, '2'),
        '3': (3, 3, '3'),
        '4': (4, 4, '4'),
        '5': (5, 5, '5'),
        '6': (6, 6, '6'),
        '7': (7, 7, '7'),
        '8': (8, 8, '8'),
        '9': (9, 9, '9'),
        '10': (10, 10, '10'),
        'Jack': (10, 10,'J'),
        'Queen': (10, 10,'Q'),
        'King': (10, 10,'K')
    }
    
    # Dictionary of the three possible suits.
    suits = {
        'Clubs': 'C',
        'Diamonds': 'D',
        'Hearts': 'H',
        'Spades':'S'
    }
    
    # Constructor for a card. Must have a number, suit and initially flipped.
    def __init__(self, number, suit, flipped = False):
        '''
        Class constructor:
        
        INPUT:
            - number: The symbolic and possible numerical values of the card, 3-tuple.
            - suit: The suit of the card.
            - flipped: If the card is flipped or not; card is initially not flipped by default.
        '''
        self.number = number
        self.suit = suit
        self.flipped = flipped
    
    # Flips the card.
    def flip_card(self):
        '''
        Flips the card.
        '''
        self.flipped = (not self.flipped)
   
    # Returns if the card is an ace.
    def is_ace(self):
        '''
        Returns if the card itself is an ace, regardless of suit.
        
        OUTPUT:
            - If the card is an ace (True) or not (False).
        '''
        return self.number[2] == Card.numbers['Ace'][2]
    
    # Returns the suit of the card.
    def suit_of_card(self):
        '''
        Returns the suit of the card.
        
        OUTPUT:
            - The suit of the card ('H','D','S','C').
        '''
        return self.suit
    
    # Returns the card type.
    def type_of_card(self):
        '''
        Returns the type of the card.
        
        OUTPUT:
            - The card type ('A', '2', '3',...,'K').
        '''
        return self.number[2]
    
    # Gets the selected value of the card.
    def value_of_card(self, val):
        '''
        Returns the selected value of the card.
        INPUT:
            -val: The first or second possible value of the card; particularly useful for the Ace (1,11).
        
        OUTPUT:
            - Returns the selected value of the card.
        '''
        return self.number[val]
    
    # Function to compare objects by their attributes.
    def __eq__(self, other):
        '''
        Tests if two cards are the same.
        OUTPUT:
            - If two cards are equal, they can take the same numerical and symbolical values,
              and suit.
        '''
        # Compare the attributes
        is_equal = True
        
        # First see if it's another card.
        if not isinstance(other, Card):
            # Dont' compare to other types
            return NotImplemented
        
        # Test that the card numbers are the same
        for i,_ in enumerate(self.number):
            is_equal = is_equal and self.number[i] == other.number[i]
        
        # Test the suit is the same, no need to compare if the cards are in the same flipped state.
        return is_equal and (self.suit == other.suit)
    
    # Function that returns a string representing the card.
    def __str__(self):
        '''
        Returns the card number and suit:
        OUPUT:
            - A string formatted with the symbolic (N) value and suit (S) as (N-S)
        '''
        return str(self.number[2]) + '-' + str(self.suit)
        