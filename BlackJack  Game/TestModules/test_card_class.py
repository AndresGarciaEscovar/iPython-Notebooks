# Import the package from the parent folder.
import os,sys,inspect
current_dir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir) 
import card

# Import the test unit.
import unittest

class test_card_class(unittest.TestCase):
    
    # Test the ace card
    def test_ace_card(self):
        '''
        Tests if that the values for the ace card are different
        '''
        # Create a test card.
        crd = card.Card(card.Card.numbers['Ace'], card.Card.suits['Clubs'])
        
        # Test the possible values of the card.
        self.assertEqual(crd.value_of_card(0), 1)
        self.assertEqual(crd.value_of_card(1), 11)
        
        # Test the card type it should return.
        self.assertEqual(crd.type_of_card(), 'A')
        
        # Test the card is initially not flipped.
        self.assertFalse(crd.flipped)
        
        # Flip the card, the card must be flipped.
        crd.flip_card()
        
        # Test if the card has been flipped.
        self.assertTrue(crd.flipped)
        
        # Test the suit.
        self.assertEqual(crd.suit_of_card(),'C')
        
    # Test the Jack, King and Queen
    def test_face_cards(self):
        '''
        Tests if that the values for the ace card are different
        '''
        # Create a test card
        crd1 = card.Card(card.Card.numbers['Jack'], card.Card.suits['Diamonds'])
        crd2 = card.Card(card.Card.numbers['Queen'], card.Card.suits['Spades'])
        crd3 = card.Card(card.Card.numbers['King'], card.Card.suits['Hearts'])
        
        # Test the possible values of the card
        self.assertEqual(crd1.value_of_card(0), 10)
        self.assertEqual(crd1.value_of_card(1), 10)
        
        # Test the possible values of the card
        self.assertEqual(crd2.value_of_card(0), 10)
        self.assertEqual(crd2.value_of_card(1), 10)
        
        # Test the possible values of the card
        self.assertEqual(crd3.value_of_card(0), 10)
        self.assertEqual(crd3.value_of_card(1), 10)
        
        # Test the card type it should return
        self.assertEqual(crd1.type_of_card(), 'J')
        self.assertEqual(crd2.type_of_card(), 'Q')
        self.assertEqual(crd3.type_of_card(), 'K')
        
        # Test the suit.
        self.assertEqual(crd1.suit_of_card(),'D')
        self.assertEqual(crd2.suit_of_card(),'S')
        self.assertEqual(crd3.suit_of_card(),'H')
    
    # Test the proper numbers on the other cards
    def test_number_cards(self):
        '''
        Tests if that the values for the ace card are different
        '''
        # Create the test cards
        crd = [ card.Card(card.Card.numbers['' + str(x)], card.Card.suits['Diamonds']) for x in range(2,11)]
        
        # Test each card
        for i, x in enumerate(crd):
            
            # Test that the value of the cards
            self.assertEqual(x.value_of_card(0), i+2)
            self.assertEqual(x.value_of_card(1), i+2)
            
            # Test the card type it should return
            self.assertEqual(x.type_of_card(), str(i+2))
            
            # Test the card is initially not flipped
            self.assertFalse(x.flipped)
        
if __name__=='__main__':
    unittest.main()