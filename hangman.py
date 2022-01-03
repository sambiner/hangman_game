"""
Name: Sam Biner
Date:  11/22/2021
Description:
"""

from random import randrange
from graphics import *
import time


# -----------------------------------
# Helper code: import hangman words

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    # in_file: file
    in_file = open('words.txt')
    # line: string
    line = in_file.readline()
    # wordlist: list of strings
    wordlist = line.split()
    return wordlist

# load the dictionary of words and point to it with
# the words_dict variable so that it can be accessed from anywhere
# in the program
words_dict = load_words()

# Run get_word() within your program to generate a random secret word
# by using a line like this within your program:
# secret_word = get_word()
def get_word():
    """
    Returns a random word from the word list
    """
    word = words_dict[randrange(0, len(words_dict))]
    return word

# end of helper code
# -----------------------------------

# CONSTANTS
MAX_GUESSES = 6

# GLOBAL VARIABLES
win = GraphWin('Hangman', 500, 500)

####### HangmanBoard Class: ######
# You will mostly not change this class, but you should understand how it works!
# You will need to use this class and its methods in play_hangman().
# The only functions you will change/add are at the bottom of the class and
# have comments that say # YOUR CODE HERE
class HangmanBoard(object):
    def __init__(self):
        self.entryBox = Entry(Point(300, 300), 10)
        self.usedLetters = Text(Point(350, 230), '')
        self.guess = Text(Point(200, 400), '- - - - - - -')
        self.textPrompt = Text(Point(250,50), 'Welcome! Please guess a single letter inside the guess box')

        self.draw_post()
        self.draw_input()
        self.textPrompt.draw(win)

    # create hangman post
    def draw_post(self):
        post = Line(Point(25, 100), Point(25, 300))
        post.setWidth(5)
        post.draw(win)

        overhang = Line(Point(25, 100), Point(125, 100))
        overhang.setWidth(2)
        overhang.draw(win)

        rope = Line(Point(100, 100), Point(100, 150))
        rope.draw(win)

    # create graphics for rest of the game input/output
    def draw_input(self):
        self.entryBox.draw(win)
        self.usedLetters.draw(win)
        self.guess.setSize(20)
        self.guess.draw(win)

        self.usedLettersText = Text(Point(350, 200), 'Used Letters:')
        self.usedLettersText.draw(win)

        # create the guess box and button
        self.guessBox = Rectangle(Point(350, 290), Point(490, 310))
        self.guessBox.setFill('white')
        self.guessBox.draw(win)
        self.guessButton = Text(Point(420, 300) , 'CLICK TO GUESS')
        self.guessButton.draw(win)

    # update the used letters text with a new set of used letters
    # letters should be a string
    def update_letters_guessed(self, letters):
        self.usedLetters.setText(letters)

    # clear the entry box
    def clear_entry(self):
        self.entryBox.setText('')

    # update the guess text
    # text should be a string
    def update_guess(self, text):
        self.guess.setText(text)

    # returns the text of the entry box after the user clicks enter
    def get_guess_entry(self):
        word = ""
        while True:
            p = win.getMouse()
            x = p.getX()
            y = p.getY()
            if x < 450 and x > 350:
                if y < 310 and y > 290:
                    word = self.entryBox.getText()
                    break
        return word

    # draw the first part of the hangman, i.e., the head
    def draw_first_invalid_guess(self):
        #YOUR CODE HERE will replace the pass call
        head = Circle(Point(100, 175), 25)
        eye1 = Circle(Point(110, 170), 1.5)
        eye2 = Circle(Point(90, 170), 1.5)
        mouth = Line(Point(92, 190), Point(108, 190))

        mouth.draw(win)
        eye2.draw(win)
        eye1.draw(win)
        head.draw(win)

    # draw the second part of the hangman, i.e., the body
    def draw_second_invalid_guess(self):
        #YOUR CODE HERE will replace the pass call
        body = Rectangle(Point(95, 200), Point(105, 275))
        body.draw(win)

    # draw the third part of the hangman, i.e., arm 1
    def draw_third_invalid_guess(self):
        #YOUR CODE HERE will replace the pass call
        arm1 = Line(Point(95, 210), Point(75, 240))
        arm1.setWidth(2)
        arm1.draw(win)

    # draw the fourth part of the hangman, i.e., arm 2
    def draw_fourth_invalid_guess(self):
        #YOUR CODE HERE will replace the pass call
        arm2 = Line(Point(105, 210), Point(125, 240))
        arm2.setWidth(2)
        arm2.draw(win)

    # draw the fifth part of the hangman, i.e., leg 1
    def draw_fifth_invalid_guess(self):
        #YOUR CODE HERE will replace the pass call
        leg1 = Line(Point(95, 270), Point(70, 295))
        leg1.setWidth(2)
        leg1.draw(win)

    # draw the sixth part of the hangman, i.e., leg 2
    def draw_sixth_invalid_guess(self):
        #YOUR CODE HERE will replace the pass call
        leg2 = Line(Point(105, 270), Point(120, 295))
        leg2.setWidth(2)
        leg2.draw(win)

    # given the number of mistakes at the invalid guess, draw the correct
    # hangman part
    def invalid_guess(self, mistakes):
        #YOUR CODE HERE will replace the pass call
        if mistakes == 1:
            self.draw_first_invalid_guess()
        elif mistakes == 2:
            self.draw_second_invalid_guess()
        elif mistakes == 3:
            self.draw_third_invalid_guess()
        elif mistakes == 4:
            self.draw_fourth_invalid_guess()
        elif mistakes == 5:
            self.draw_fifth_invalid_guess()
        elif mistakes == 6:
            self.draw_sixth_invalid_guess()
        else:
            print('You Failed!')


    def update_output_text(self, text):
        self.textPrompt.setText(text)


def word_guessed(secret_word, letters_guessed):
    """
    Returns True if the player has successfully guessed the word,
    and False otherwise.
    """
    ####### YOUR CODE HERE ######
    for letter in secret_word:
        if letter not in letters_guessed:
           return False
    return True



def get_guessed(secret_word, letters_guessed):
    """
    Returns the characters you have guessed in the secret word so far,
    with dashes (-) for characters that haven't been guessed.
    For example, if the word is claptrap and you have guessed only 'a',
    it should return --a---a-
    """
    ####### YOUR CODE HERE ######
    guessed = []
    for letter in secret_word:
        if letter in letters_guessed:
            guessed.append(letter)
        elif letter not in letters_guessed:
            guessed.append('-')
    return guessed




def play_hangman():
    # Actually play the hangman game

    # GAME VARIABLES
    secret_word = get_word()
    letters_guessed = []
    mistakes_made = 0

    # create an instance of the hangman board
    h = HangmanBoard()
    #print(get_guessed(secret_word, ['c', 'z', 'p', 'm']))
    ####### YOUR CODE HERE #####
    # Get a random secret word for extra credit
    # For development, it is ok to use a hardcoded word
    # continually loop:
      #update guessed word so far
      #update used letters
    while True:
        letter = h.get_guess_entry().lower()
        if 'a' <= letter <= 'z':

            if len(letter) == 1:

                if letter in secret_word:

                    if letter in letters_guessed:
                        mistakes_made += 1
                        letters_guessed.append(letter)
                        h.update_guess(get_guessed(secret_word, letters_guessed))
                        h.update_letters_guessed(letters_guessed)
                        h.update_output_text('Invalid guess, guess again')
                        if mistakes_made >= 6:
                            h.draw_sixth_invalid_guess()
                            h.update_output_text('Darn it! You lost :(')
                            print('The secret word was', secret_word)
                            time.sleep(3)
                            win.close()
                        h.invalid_guess(mistakes_made)

                    if letter not in letters_guessed:
                        letters_guessed.append(letter)
                        h.update_guess(get_guessed(secret_word, letters_guessed))
                        h.update_letters_guessed(letters_guessed)
                        h.update_output_text('Yay! Letter found')
                        if word_guessed(secret_word, letters_guessed):
                            h.update_output_text('You won! Congrats')
                            time.sleep(3)
                            win.close()

                elif letter not in secret_word:
                    mistakes_made += 1
                    letters_guessed.append(letter)
                    h.update_guess(get_guessed(secret_word, letters_guessed))
                    h.update_letters_guessed(letters_guessed)
                    h.update_output_text('Invalid guess, guess again')
                    if mistakes_made >= 6:
                        h.draw_sixth_invalid_guess()
                        h.update_output_text('Darn it! You lost :(')
                        print('The secret word was', secret_word)
                        time.sleep(3)
                        win.close()
                    h.invalid_guess(mistakes_made)

                h.clear_entry()

        if len(letter) >= 2:
            h.update_output_text('Please only input one character!')
            h.clear_entry()

# main calls
play_hangman()
win.mainloop()
