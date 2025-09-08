import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1)  # 0 is tails, 1 is heads
# Map guess to int
guess_int = 1 if guess =='heads' else 0

if toss == guess_int:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    guess_int =1 if guess == 'heads' else 0
    if toss == guess_int:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')