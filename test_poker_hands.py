import unittest
import sys

from poker_hands import *
class TestPokerHands(unittest.TestCase):

    # A, K, Q, J, 10, all of the same suit.
    def test_royal_flush(self):
        print("\nTesting Royal Flush...")

        hand = ['AH', 'TH', 'JH', 'QH', 'KH']
        print(f"{hand} is a Royal Flush.")
        self.assertTrue(check_royal_flush(hand))

        hand = ['5H', '6H', '7H', '8H', '9H']
        print(f"{hand} is NOT a Royal Flush.")
        self.assertFalse(check_royal_flush(hand))

    # Five consecutive cards of the same suit.
    def test_straight_flush(self):
        print("\nTesting Straight Flush...")
        
        hand = ['5H', '6H', '7H', '8H', '9H']
        print(f"{hand} is a Straight Flush.")
        self.assertTrue(check_straight_flush(hand))

        hand = ['5S', '6S', '7S', '8S', '10S']
        print(f"{hand} is NOT a Straight Flush.")
        self.assertFalse(check_straight_flush(hand))

    # Four cards of the same rank.
    def test_four_of_a_kind(self):
        print("\nTesting Four of a Kind...")
        
        hand = ['5H', '5D', '5S', '5C', '9H']
        print(f"{hand} is a Four of a Kind.")
        self.assertTrue(check_four_of_a_kind(hand))

        hand = ['5H', '6D', '7S', '8C', '9H']
        print(f"{hand} is NOT a Four of a Kind.")
        self.assertFalse(check_four_of_a_kind(hand))

    # Three of a kind plus a pair.
    def test_full_house(self):
        print("\nTesting Full House...")
        
        hand = ['5H', '5D', '5S', '9C', '9H']
        print(f"{hand} is a Full House.")
        self.assertTrue(check_full_house(hand))

        hand = ['5H', '6D', '7S', '8C', '9H']
        print(f"{hand} is NOT a Full House.")
        self.assertFalse(check_full_house(hand))

    # Five cards of the same suit, not in sequence.
    def test_flush(self):
        print("\nTesting Flush...")
        
        hand = ['5H', '6H', '7H', '8H', '9H']
        print(f"{hand} is a Flush.")
        self.assertTrue(check_flush(hand))

        hand = ['5S', '6H', '7H', '8H', '9H']
        print(f"{hand} is NOT a Flush.")
        self.assertFalse(check_flush(hand))

    # Five consecutive cards of different suits.
    def test_straight(self):
        print("\nTesting Straight...")
        
        hand = ['5H', '6D', '7S', '8C', '9H']
        print(f"{hand} is a Straight.")
        self.assertTrue(check_straight(hand))

        hand = ['5H', '6H', '7H', '9H', 'TH']
        print(f"{hand} is NOT a Straight.")
        self.assertFalse(check_straight(hand))

    # Three cards of the same rank.
    def test_three_of_a_kind(self):
        print("\nTesting Three of a Kind...")
        
        hand = ['5H', '5D', '5S', '8C', '9H']
        print(f"{hand} is a Three of a Kind.")
        self.assertTrue(check_three_of_a_kind(hand))

        hand = ['5H', '6D', '7S', '8C', '9H']
        print(f"{hand} is NOT a Three of a Kind.")
        self.assertFalse(check_three_of_a_kind(hand))

    # Two different pairs.
    def test_two_pairs(self):
        print("\nTesting Two Pairs...")
        
        hand = ['5H', '5D', '7S', '7C', '9H']
        print(f"{hand} is a Two Pairs.")
        self.assertTrue(check_two_pairs(hand))

        hand = ['5H', '6D', '7S', '8C', '9H']
        print(f"{hand} is NOT a Two Pairs.")
        self.assertFalse(check_two_pairs(hand))

    # Two cards of the same rank.
    def test_one_pair(self):
        print("\nTesting One Pair...")
        
        hand = ['5H', '5D', '7S', '8C', '9H']
        print(f"{hand} is a One Pair.")
        self.assertTrue(check_one_pairs(hand))

        hand = ['5H', '6D', '7S', '8C', '10H']
        print(f"{hand} is NOT a One Pair.")
        self.assertFalse(check_one_pairs(hand))


def run_tests():
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(sys.modules[__name__])
    runner = unittest.TextTestRunner(stream=sys.stdout)
    return runner.run(suite)
