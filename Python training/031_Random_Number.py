# Random Numbers

import random # use this function to random things

#print(help(random))

low = 1
high = 10
options = ("rock", "paper", "scissor")
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]


number = random.randint(low, high)
print(number)

number = random.random()
print(number)

options = random.choice(options)
print(options)

random.shuffle(cards)
print(cards)