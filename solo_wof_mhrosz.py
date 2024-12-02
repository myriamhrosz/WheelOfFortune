"""
Author: Myriam Hrosz, mhrosz@purdue.edu
Assignment: 12.1 - Solo WOF
Date: 12/18/2021

Description:
    SIngle player game of wheel of fortune combined with hangman.

Contributors:none
    Name, login@purdue.edu [repeat for each]

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""
import random as r
import string


def load_phrases():
    text = []
    with open('phrases.txt') as phrases:
        for lines in phrases:
            lines = lines.rstrip()
            text.append(lines)
    phrases = r.sample(text, k=len(text))
    return phrases

# Actions to be taken during round


def spin_the_wheel():
    # 21 spaces
    spaces = [500, 500, 500, 500, 550, 550, 600, 600, 600, 600, 650,
              650, 650, 700, 700, 800, 800, 900, 2500, 'BANKRUPT', 'BANKRUPT']
    spin = r.choice(spaces)
    return spin

def solowof(r, new, Vs, Cs,roundmoney):
    vs = ''.join(Vs).upper()
    cs = ''.join(Cs).upper()
    r_money= "${:,d}".format(roundmoney)
    print(f':: Solo WoF :::::::::::::::::::::::::::::: Round {r+1} of 4 ::')
    print(f'::{new.center(54)}::')
    print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::')
    print(f'::{vs.center(11)}::{cs.center(27)}::{r_money:>11} ::')
    print('::::::::::::::::::::::::::::::::::::::::::::::::::::::::::\n')
    print('Menu:\n  1 - Spin the wheel.\n  2 - Buy a vowel.\n  3 - Solve the puzzle.\n  4 - Quit the game.\n')


def main():
    alphabet_string = string.ascii_lowercase
    abcs = list(alphabet_string)
    
    # Open Text file
    # Load all the text from the phrases file into a list called text

    # Run four rounds of the game
    print('Welcome to Solo Wheel of Fortune\n')
    # Set total winnings to 0
    total = 0
    roundmoney = 0
    x = 0
    phrases = load_phrases()
    for ra in range(4):
        # Select i phrase from the list
        phrase = phrases[x].lower()
        x+=1
        # Save what phrase has been selected
        keep = phrase
        # Replace all letters with underscores
        for i in range(len(phrase)):
            for letters in abcs:
                new = (phrase.replace(letters, '_'))
                phrase = new
        total += roundmoney
        roundmoney = 0
        V = ['a', 'e', 'i', 'o', 'u']
        Vs = ['a', 'e', 'i', 'o', 'u']
        C = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
          'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
        Cs = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
          'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
        while (True):
            solowof(ra, new, Vs, Cs,roundmoney)
            menu = input('Enter the number of your choice: ')
            # Spin the Wheel
            if menu == '1':
                # Check there are enough consonants
                if not bool([let for let in Cs if(let in C)]):
                    print('There are no more consonants to choose.\n')
                elif len(Cs) > 0:
                    spin = spin_the_wheel()
                    if spin == 'BANKRUPT':
                        print(f'The wheel landed on {spin}.')
                        print(f'You lost ${roundmoney:,d}!\n')
                        roundmoney=0
                    else:
                        print(f'The wheel landed on ${spin:,d}.')
                        # Ask for consonant
                        while(True):
                            cons = input('Pick a consonant: ')
                            cons = cons.lower()
                            # Error if consonant is vowel
                            if cons in V:
                                print('Vowels must be purchased.')
                            #Error if multiple letters
                            elif len(cons) > 1 or cons == " " or cons == "":
                                print('Please enter exactly one character.')
                            # elif cons == '4':
                            #     menu = '4'
                            #     break
                            # Error if consonant is number
                            elif not cons.isalpha():
                                print(f'The character {cons} is not a letter.')
                            # Error if consonant has already been used
                            elif cons not in Cs:
                                cons=cons.upper()
                                print(f'The letter {cons} has already been used.')
                            
                            # If not used and consonant
                            elif cons in Cs:
                                # replace the letter in the phrase and take out of consonant list 
                                count = 0
                                temp = Cs.index(cons)
                                Cs[temp] = ' '
                                for i in range(len(keep)):
                                    if keep[i]==cons:
                                        list1 = list(new)
                                        list1[i] = cons.upper()
                                        new = ''.join(list1)
                                        count+=1
                                cons = cons.upper()
                                if count > 1:
                                    print(f'There are {count} {cons}\'s, which earns you ${count*spin:,d}.\n')
                                    roundmoney += count*spin
                                elif count == 1:
                                    print(f'There is {count} {cons}, which earns you ${spin:,d}.\n')
                                    roundmoney += spin
                                else:
                                    print(f'I\'m sorry, there are no {cons}\'s.\n')
                                break
            # Buy a vowel
            if menu == '2':
                # ensure there are still vowels left
                if not bool([let for let in Vs if(let in V)]):
                    print('There are no more vowels to buy.\n')
                elif len(Vs) > 0:
                    # Ensure there is enough round money to buy a vowel
                    if roundmoney >=275:
                        while (True):                    
                            vowel = input('Pick a vowel: ')
                            vowel=vowel.lower()
                            # Error if too many or too little letters
                            if len(vowel) > 1 or vowel == " " or vowel == "":
                                print('Please enter exactly one character.')
                            # Error if consonant
                            elif vowel in C:
                                print('Consonants cannot be purchased.')
                            # Error if not letter
                            elif not vowel.isalpha():
                                print(f'The character {vowel} is not a letter.')
                            
                            # Error if already bought
                            elif vowel not in Vs:
                                vowel = vowel.upper()
                                print(f'The letter {vowel} has already been purchased.')
                            
                            # Ensure that vowel is left
                            elif vowel in Vs:
                                roundmoney = roundmoney - 275
                                count = 0
                                # Remove vowel from list
                                temp = Vs.index(vowel)
                                Vs[temp] = ' '
                                # Check if the vowel is in the phrase
                                for i in range(len(keep)):
                                    if keep[i]==vowel:
                                        list1 = list(new)
                                        list1[i] = vowel.upper()
                                        new = ''.join(list1)
                                        count+=1
                                vowel = vowel.upper()
                                if count > 1:
                                    print(f'There are {count} {vowel}\'s.\n')
                                elif count == 1:
                                    print(f'There is {count} {vowel}.\n')
                                else:
                                    print(f'I\'m sorry, there are no {vowel}\'s.\n')
                                break
                    elif roundmoney < 275:
                        print('You need at least $275 to buy a vowel.\n')
                        continue

            # Guess Solution
            if menu == '3':
                print(f'Enter your solution.\n  Clues: {new}')
                guess = input('  Guess: ').lower()
                if guess == keep:
                    print('Ladies and gentlemen, we have a winner!')
                    # If they win and have less than round up to 1000
                    if roundmoney <1000:
                        roundmoney = 1000
                # elif guess == '4':
                #     menu = '4'
                #     break
                else:
                    keep = keep.upper()
                    print(f'I\'m sorry. The correct solution was:\n{keep}')
                    roundmoney = 0
                print(f'\nYou earned ${roundmoney:,d} this round.\n')
                break
            # Invalid menu choices
            if menu.isalpha() or (menu != '4' and menu != '3' and menu != '2' and menu != '1'):
                print(f'\"{menu}\" is an invalid choice.')
                continue
            # Quit Round
            if menu == '4':
                print(f'\nYou earned $0 this round.\n')
                break
        if menu == '4':
            break
    if menu =='4':
        exit
    
              
    print(f'Thanks for playing!\nYou earned a total of ${total:,d}.')
    # comma at third house
    # When quit - quit everything not just round
    # dollar sign in main print section


if __name__ == '__main__':
    main()
