from flask import Flask, request, render_template, redirect, url_for, jsonify
from enum import Enum, auto
from poker_hands import *

import random
import os
import sys
import io
import secrets


app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
suits = ['Heart', 'Diamond', 'Club', 'Spade']


# Create labels foreach of the winning poker hands
class PokerHand(Enum):
    ROYAL_FLUSH = ("Royal Flush", auto())
    STRAIGHT_FLUSH = ("Straight Flush", auto())
    FOUR_OF_A_KIND = ("Four of a Kind", auto())
    FULL_HOUSE = ("Full House", auto())
    FLUSH = ("Flush", auto())
    STRAIGHT = ("Straight", auto())
    THREE_OF_A_KIND = ("Three of a Kind", auto())
    TWO_PAIRS = ("Two Pairs", auto())
    ONE_PAIR = ("One Pair", auto())
    PAIR = ("Pair", auto())

# Generate the full deck of 52 cards
def generate_deck():
    numbers = list(range(1, 14))
    
    deck = []
    
    for suit in suits:
        for number in numbers:
            card = (number, suit)
            deck.append(card)
            
    return deck

deck = generate_deck()

@app.route('/')
def index():
    print(deck)
    # A dictionary to map numbers to their corresponding names
    number_to_name = {
        11: 'JACK',
        12: 'QUEEN',
        13: 'KING'
    }

    # Base path for the card images
    base_path = "cards/"

    # Generate the cards array using list comprehension and enumerate
    cards = [
        {
            'id': index + 1, 
            'suit': suit,
            'number': number,
            'filename': f"{base_path}{suit.upper()}-{number}" + (f"-{number_to_name[number].upper()}" if number in number_to_name else "") + ".svg"
        }
        for index, (number, suit) in enumerate(deck)
    ]

    return render_template('./index.html', cards=cards, suits=suits)


@app.route('/process', methods=['POST'])
def process():
    selected_card_ids = request.form.getlist('selected_cards')
    print(selected_card_ids)
    
    if len(selected_card_ids) != 5:
        return jsonify(status="error", message="Please select 5 cards.")
    
    winning_hand = is_winning_set(selected_card_ids)
    if winning_hand:
        return jsonify(status="success", message="Congratulations! You have a winning set!", winning_set=winning_hand.value[0])
    else:
        return jsonify(status="error", message="Sorry, not a winning set.")


def is_winning_set(selected_card_ids):
    hand = process_card_ids_into_hand(selected_card_ids)
    print(hand)
    # Define your logic to determine if the given cards form a winning set
    if check_royal_flush(hand):
        return PokerHand.ROYAL_FLUSH
    if check_straight_flush(hand):
        return PokerHand.STRAIGHT_FLUSH
    if check_four_of_a_kind(hand):
        return PokerHand.FOUR_OF_A_KIND
    if check_full_house(hand):
        return PokerHand.FULL_HOUSE
    if check_flush(hand):
        return PokerHand.FLUSH
    if check_straight(hand):
        return PokerHand.STRAIGHT
    if check_three_of_a_kind(hand):
        return PokerHand.THREE_OF_A_KIND
    if check_two_pairs(hand):
        return PokerHand.TWO_PAIRS
    if check_one_pairs(hand):
        return PokerHand.ONE_PAIR
    return False


def process_card_ids_into_hand(ids):
    # Extract the relevant cards based on the provided IDs
    selected_cards = [deck[int(i)-1] for i in ids]  # Subtracting 1 since list indices start from 0
    
    # Convert the card details into the desired format
    hand = []
    for number, suit in selected_cards:
        suit_initial = suit[0]
        start = number
        if number == 1: start = 'A'
        elif number == 10: start = 'T'
        elif number == 11: start = 'J'
        elif number == 12: start = 'Q'
        elif number == 13: start = 'K'
        
        hand.append(f"{start}{suit_initial}")

    return hand


@app.route('/run-tests')
def run_tests():
    # Redirect stdout to capture the test results
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout

    # Import and run the tests
    from test_poker_hands import run_tests as execute_tests
    execute_tests()

    # Reset stdout to its original state
    sys.stdout = old_stdout
    test_results = new_stdout.getvalue()

    return render_template('test_results.html', test_results=test_results)


if __name__ == "__main__":
    app.run(debug=True)
