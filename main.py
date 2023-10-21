from flask import Flask, request, render_template, redirect, url_for, jsonify

import random
import os
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)
suits = ['Heart', 'Diamond', 'Club', 'Spade']

def generate_deck():
    numbers = list(range(1, 14))
    
    deck = []
    
    for suit in suits:
        for number in numbers:
            card = (number, suit)
            deck.append(card)
            
    return deck

# Test the function
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
    
    if len(selected_card_ids) < 5:
        return jsonify(status="error", message="Please select 5 cards.")
    
    if is_winning_set(selected_card_ids):
        return jsonify(status="success", message="Congratulations! You have a winning set!")
    else:
        return jsonify(status="error", message="Sorry, not a winning set.")


def is_winning_set(cards):
    # Define your logic to determine if the given cards form a winning set
    # For now, it's just a placeholder function
    return False

if __name__ == "__main__":
    app.run(debug=True)
    print(deck)
