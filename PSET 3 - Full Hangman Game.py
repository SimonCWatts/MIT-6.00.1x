# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    return all([False for letter in secretWord if letter not in lettersGuessed])



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    return ''.join(letter if letter in lettersGuessed else ' _ ' for letter in secretWord)


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    return ''.join([letter for letter in 'abcdefghijklmnopqrstuvwxyz' if letter not in lettersGuessed])
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    
    # make a list to store the letters that have been guess already
    lettersGuessed = []
    
    # store the number of incorrect guesses made so far
    mistakesMade = 0
    
    # a string of the letter than have not been chosen yet
    availableLetters = getAvailableLetters(lettersGuessed)
    
    # start with eight guesses
    remainGuesses = 8
    
    # string input from user
    guess = ''
    
    def makeGuess():    
        '''
        asks for a user input
        returns the lower case of the value entered
        '''
        # ask player for a guess
        guess = input('Please guess a letter: ')
        
        #convert the guess into lower case
        guessInLowerCase = guess.lower()
        
        return guessInLowerCase

    # START THE GAME!!
    print('Welcome to the game, Hangman!\nI am thinking of a word that is', len(secretWord), 'letters long.')
    print('-------------')

    while remainGuesses > 0:
            
        # 1. ask for user input
        print('You have', remainGuesses, 'guesses left.' )
        print('Available letters:', getAvailableLetters(lettersGuessed))
        guess = makeGuess()
        
        # 2. now check the guess has not already been chosed..
        if guess in lettersGuessed:
            print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
            print('-------------')
        # 3. check if the guess was correct
        elif guess in secretWord:
         # 4. update checked list
            lettersGuessed += guess
         # 6. update guessed word
            getGuessedWord(secretWord, lettersGuessed)
            print("Good guess:", getGuessedWord(secretWord, lettersGuessed))
            print('-------------')
        else:
        # 4. update checked list
            lettersGuessed += guess
        # 5. update number of guesses
            remainGuesses -= 1
            print('Oops! That letter is not in my word:', getGuessedWord(secretWord, lettersGuessed))
            print('-------------')
    
        # 7. if all letter are found, then win the game
        if getGuessedWord(secretWord, lettersGuessed) == secretWord:
            print('Congratulations, you won!')
            return 1
        
    print('Sorry, you ran out of guesses. The word was', secretWord)
    return 0

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
