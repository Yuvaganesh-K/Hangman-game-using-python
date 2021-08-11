# library that we use in order to choose on random words from a list of words
import random

# Here the user is asked to enter the name first
name = input("What is your name?")

print("Good Luck {0} !! ".format(name))

words = list()
WORDLIST = 'wordlist.txt'
f = open(WORDLIST, 'r')
for item in f:
    item = item.strip().lower()
    words.append(item)

# Function will choose one random word from this list of words
word = random.choice(words)

guesses = ''

# any limits for the number of turns can be set here
while True:
    turns = int(input('Enter number of chances you want [min:2,max:12]:'))
    if turns < 2 or turns > 12:
        print('Please enter within the specified values!')
    else:
        break
print("Game has begun. Guess the characters:-")
while turns > 0:
    # counts the number of times a user fails
    failed = 0

    # all characters from the input word taking one at a time.
    for char in word:

        # comparing that character with the character in guesses
        if char in guesses:
            print(char, end='')
        else:
            print('_', end='')
            # for every failure 1 will be incremented in failure
            failed += 1

    if failed == 0:
        # user will win the game if failure is 0 and 'You Win' will be given as output
        print('\r')
        print("You Win")
        # this prints the correct word. Not mandatory to include this line.
        print("The word is '{0}'".format(word))
        break

    print('\r')

    # if user has input the wrong alphabet then it will ask user to enter another alphabet#
    guess = input("guess a character:")
    guess = guess.lower()

    # every input character will be stored in guesses
    guesses += guess

    # check input with the character in word
    if guess in word:
        print('Right')
        print('You have {0} more guesses'.format(turns))
    elif guess not in word:
        turns -= 1
        # if the character doesn’t match the word then “Wrong” will be given as output
        print("Wrong")

        # this will print the number of turns left for the user
        print('You have {0} more guesses'.format(turns))
    if turns == 0:
        print("You Loose!! Better luck next time!!")
        print('The word is "{0}"'.format(word))































































































































