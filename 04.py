import re
from collections import deque

with open('./inp/04.txt') as f:
    cards = f.read().split('\n')

set_nos = lambda x: set(map(int, x.strip().split()))

########
# Part A
########

points = 0
for card in cards:
    card_id, winning_no, my_no = re.match(r'Card[\s]+(\d+): ([\d\s]+)\| ([\d\s]+)', card).groups()
    winning_no = set_nos(winning_no); my_no = set_nos(my_no)
    matches = len(winning_no.intersection(my_no))
    if matches > 0:
        points += int(2**(matches - 1))

print(points)

########
# Part B
########

class Card:
    def __init__(self, id, winning_numbers, my_numbers):
        self.id = id
        self.winning_numbers = winning_numbers
        self.my_numbers = my_numbers
    def __str__(self): 
        return f'{self.id}: {self.winning_numbers} | {self.my_numbers}'
    def __repr__(self):
        return str(self)

id_to_cards = {}
for card in cards:
    card_id, winning_no, my_no = re.match(r'Card[\s]+(\d+): ([\d\s]+)\| ([\d\s]+)', card).groups()
    winning_no = set_nos(winning_no); my_no = set_nos(my_no)
    id_to_cards[int(card_id)] = Card(int(card_id), winning_no, my_no)

cycles = 0
queue = deque(id_to_cards.values())
while len(queue):
    card = queue.popleft()
    cycles += 1
    matches = len(card.winning_numbers.intersection(card.my_numbers))
    for id in range(card.id + 1, card.id + 1 + matches):
        queue.append(id_to_cards[id])

print(cycles)