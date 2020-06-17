# Import the package from the parent folder.
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
import deck
import card

# Import the test unit.
import unittest

class test_deck_class(unittest.TestCase):

    # Deck creation
    def test_deck_length(self, new_deck = None):
        '''
        Tests that a deck with 52 unique cards has been created.
        '''
        # Get the deck to be tested
        dck = new_deck 
        
        # If the value is None, create new deck.
        if dck == None :
            # Create a new deck.
            dck = deck.Deck()
            
        # Test the length of the deck
        self.assertEqual(len(dck.cards), 52)
    
    # Remove a card from a deck, test deck and object extracted.
    def test_deck_pop_length(self):
        '''
        Tests if when a card is removed the deck loses one card and returns a card.
        '''
        # Create a new deck
        dck = deck.Deck()
        
        # Test that the deck has 52 cards
        self.test_deck_length(dck)
        
        # Pop out a card.
        crd = dck.get_top_card()
        crd1 = card.Card(card.Card.numbers['Ace'],card.Card.suits['Clubs'])
        
        # Check that we remove all the cards.
        i = 51
        while True:
            
            # Check that when the top card is taken and the deck is length zero we get None
            if i == 0:
                self.assertEqual(len(dck.cards), 0)
                self.assertEqual(dck.get_top_card(), None)
                break
            else:
                self.assertEqual(len(dck.cards), i)
                self.assertEqual(type(crd), type(crd1))
                i -= 1 
                
            # Take the top card.
            crd = dck.get_top_card()
        
    # Remove a card from a deck, test deck and object extracted.
    def test_unique_cards_(self):
        
        # Create a new deck
        dck = deck.Deck()
        
        # Test that there are no repeated cards.
        for i in range(0,len(dck.cards)-1):
            for j in range(i+1, len(dck.cards)):
                self.assertFalse(dck.cards[j] == dck.cards[i])
        
if __name__=='__main__':
    unittest.main()