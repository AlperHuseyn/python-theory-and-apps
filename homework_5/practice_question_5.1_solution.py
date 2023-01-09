""" Instructor solution to practice question 5.1 """
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


card_dict = {card: index for index, card in enumerate(create_deck())}


def compare_card(card):
    return card_dict[card]


def sort_cards(cards):
    cards.sort(key=compare_card)


deck = create_deck()
random.shuffle(deck)
north, east, south, west = distribute_deck(deck)

sort_cards(north)
print(north)
sort_cards(east)
print(east)
sort_cards(south)
print(south)
sort_cards(west)
print(west)
