from flask import Flask, request, render_template, redirect, url_for

import random
import os
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

def generate_deck():
    suits = ['Heart', 'Diamond', 'Club', 'Spade']
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
            'filename': f"{base_path}{suit.upper()}-{number}" + (f"-{number_to_name[number].upper()}" if number in number_to_name else "") + ".svg"
        }
        for index, (number, suit) in enumerate(deck)
    ]

    return render_template('./index.html', cards=cards)

if __name__ == "__main__":
    app.run(debug=True)
    print(deck)
