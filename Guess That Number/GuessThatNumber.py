import random

print('-------------------------')
print('----GUESS THE NUMBER-----')
print('-------------------------')

#veryrandomnumber = 43
veryrandomnumber = random.randint(0,100)

guess_text = input('Take a guess... ')
guess: int = int(guess_text)

while guess != veryrandomnumber:
    if guess < veryrandomnumber:
        message = 'Sorry, ' + guess_text + ' is lower than my number, try again: '
    else:
        message = 'Sorry, ' + guess_text + ' is higher than my number, try again: '
    guess_text = input(message)
    guess = int(guess_text)

print('CORRECT!')
