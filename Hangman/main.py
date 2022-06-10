#Hangman program

#Import and initialize the pygame library
import re  # Needed for splitting text with a regular expression
import random
import pygame
pygame.init()

# import pygame
# pygame.init()

def loadWordsFromFile(fileName):
    # Read file as a string
    fileref = open(fileName, "r")
    textData = fileref.read()
    fileref.close()

    # Split text by one or more whitespace characters
    return re.split('\s+', textData)
# end loadWordsFromFile()



def main():
    # Load data files into lists  
    dictionary = loadWordsFromFile("dictionary.txt")
    word_characters = []
    incorrect_guesses = 0

    #Start game
    random_word = random.choice(dictionary)
    for i in range(len(random_word)):
        word_characters.append(random_word[i])
        i += 1
    print(word_characters)
    loop = True
    while loop:
        #Ask user for their input

        guess = input("Please enter your guess: ")
        if guess in word_characters:
            print("Your letter was in the word!")
            word_characters.remove(guess)
            if word_characters == 0:
                print("You won!")
        else:
            print("That letter is not in the word")
            incorrect_guesses += 1
            print("This is your " + str(incorrect_guesses) + " incorrect guess")
        if incorrect_guesses == 10:
            print("Game over - You lost")
            loop = False

main()
