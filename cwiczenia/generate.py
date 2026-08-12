import random

value = random.randint(1, 10)

print(value)

cards = ["a", "b", "c"]

random.shuffle(cards)

for card in cards:

    print(card)