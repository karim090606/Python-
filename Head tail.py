print('Name:karim s mulla\nUSN: 1AY24AI052 \nSection: M\n ')
import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input().lower()
toss = random.randint(0, 1)  
toss_str = 'heads' if toss == 1 else 'tails'
if guess == toss_str:
    print('You got it!')
else:
    print('Nope! Guess again:')
    guess = input().lower()
    if guess == toss_str:
        print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
