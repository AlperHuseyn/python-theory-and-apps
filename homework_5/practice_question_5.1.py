""" My approach to practice question #5.1 """
import random


def create_deck():
    card_type = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
    card_name = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    deck = []
    for cn in card_name:
        for ct in card_type:
            deck.append(ct + '-' + cn)
    return deck


def distribute_deck(deck):
    cards = ([], [], [], [])
    for i in range(len(deck)):
        cards[i % 4].append(deck[i])

    return cards


def sort_cards(cards):
    point_values = {
        'Spades-2': 0, 'Spades-3': 1, 'Spades-4': 2, 'Spades-5': 3, 'Spades-6': 4, 'Spades-7': 5, 'Spades-8': 6,
        'Spades-9': 7, 'Spades-10': 8, 'Spades-Jack': 9, 'Spades-Queen': 10, 'Spades-King': 11, 'Spades-Ace': 12,
        'Hearts-2': 13, 'Hearts-3': 14, 'Hearts-4': 15, 'Hearts-5': 16, 'Hearts-6': 17, 'Hearts-7': 18,
        'Hearts-8': 19, 'Hearts-9': 20, 'Hearts-10': 21, 'Hearts-Jack': 22, 'Hearts-Queen': 23, 'Hearts-King': 24,
        'Hearts-Ace': 25, 'Diamonds-2': 26, 'Diamonds-3': 27, 'Diamonds-4': 28, 'Diamonds-5': 29,
        'Diamonds-6': 30, 'Diamonds-7': 31, 'Diamonds-8': 32, 'Diamonds-9': 33, 'Diamonds-10': 34,
        'Diamonds-Jack': 35, 'Diamonds-Queen': 36, 'Diamonds-King': 37, 'Diamonds-Ace': 38, 'Clubs-2': 39,
        'Clubs-3': 40, 'Clubs-4': 41, 'Clubs-5': 42, 'Clubs-6': 43, 'Clubs-7': 44, 'Clubs-8': 45, 'Clubs-9': 46,
        'Clubs-10': 47, 'Clubs-Jack': 48, 'Clubs-Queen': 49, 'Clubs-King': 50, 'Clubs-Ace': 51
    }

    rev_point_vals = {}
    for key, value in point_values.items():
        rev_point_vals[value] = key

    for i, card in enumerate(cards, 1):
        print(f'#{i}##')
        for idx, elem in enumerate(card):
            card[idx] = point_values[elem]
        card.sort()
        for ind, elem in enumerate(card):
            card[ind] = rev_point_vals.get(elem)
        print(card)


deck = create_deck()
random.shuffle(deck)
cards = distribute_deck(deck)
sort_cards(cards)