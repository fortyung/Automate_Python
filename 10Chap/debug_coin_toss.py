'''
Practice Project: Debugging Coin TOSS
'''
#! python3

import random
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)

GUESS = ''
while GUESS not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    GUESS = input().lower()
logging.debug(f"Guess is {GUESS}")

TOSS = ['heads', 'tails']
random.shuffle(TOSS)
logging.debug(f"Toss is {TOSS[0]}")

if GUESS == TOSS[0]:
    print('You got it!')
else:
    print('Nope! guess again!')
    GUESS = input().lower()
    logging.debug(f"Guess after second try is {GUESS}")

    random.shuffle(TOSS)
    logging.debug(f"Toss after second try is {TOSS[0]}")

    if GUESS == TOSS[0]:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
