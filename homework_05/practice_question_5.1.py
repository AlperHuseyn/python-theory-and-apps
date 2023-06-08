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
    point_values = {'Spades-2': 0, 'Hearts-2': 1, 'Diamonds-2': 2, 'Clubs-2': 3, 'Spades-3': 4, 'Hearts-3': 5,
                    'Diamonds-3': 6, 'Clubs-3': 7, 'Spades-4': 8, 'Hearts-4': 9, 'Diamonds-4': 10, 'Clubs-4': 11,
                    'Spades-5': 12, 'Hearts-5': 13, 'Diamonds-5': 14, 'Clubs-5': 15, 'Spades-6': 16, 'Hearts-6': 17,
                    'Diamonds-6': 18, 'Clubs-6': 19, 'Spades-7': 20, 'Hearts-7': 21, 'Diamonds-7': 22, 'Clubs-7': 23,
                    'Spades-8': 24, 'Hearts-8': 25, 'Diamonds-8': 26, 'Clubs-8': 27, 'Spades-9': 28, 'Hearts-9': 29,
                    'Diamonds-9': 30, 'Clubs-9': 31, 'Spades-10': 32, 'Hearts-10': 33, 'Diamonds-10': 34,
                    'Clubs-10': 35, 'Spades-Jack': 36, 'Hearts-Jack': 37, 'Diamonds-Jack': 38, 'Clubs-Jack': 39,
                    'Spades-Queen': 40, 'Hearts-Queen': 41, 'Diamonds-Queen': 42, 'Clubs-Queen': 43, 'Spades-King': 44,
                    'Hearts-King': 45, 'Diamonds-King': 46, 'Clubs-King': 47, 'Spades-Ace': 48, 'Hearts-Ace': 49,
                    'Diamonds-Ace': 50, 'Clubs-Ace': 51}

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