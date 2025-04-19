# -*- coding: utf-8 -*-
"""
Created on Sat Apr 19 04:53:56 2025
@author: PIOTR
"""

import random

def generate_random_number(range_min: int = 0, range_max: int = 100) -> int:
    """
    This function returns random non negative
    integer between 0 and range.
    """
    return random.randint(range_min, range_max)


def ask_to_play_again() -> bool:
    """
    Functions asks if the player wants to play again.
    """
    answer = False
    
    while True:
        try:
            input_number = int(input('Press 0 to quit, 1 to play again: '))
            
            if(input_number == 0):
                answer = False
                break
            
            elif(input_number == 1):
                answer = True
                break
                
            else:
                print('This is not a valid option.')           
        
        except ValueError:
            print('This is not a number.')
        
    
    return answer


def guess_number(number: int) -> bool:
    """
    Asks the player to try to guess the number.
    """
    is_correct = False
    
    try:
        input_number = int(input('Try to guess the number: '))
        
        if(input_number == number):
            print('Correct.')
            is_correct = True
        
        elif(input_number > number):
            print('You guessed too high.')
            
        elif(input_number < number):
            print('You guessed too low.')           
    
    except ValueError:
        print('This is not a number.')
    
    return is_correct


def ask_for_range():
    """
    Asks the player to give the range.
    """
    try:
        range_min = int(input('Give the min of the range: '))
        range_max = int(input('Give the max of the range: '))
        
        if(range_min > range_max):
            print('Min greater than max. Switching the values around')
            return range_max, range_min
        
        return range_min, range_max

    except ValueError:
        print('This is not a number. 0-100 assumed.')
        
    return 0, 100
        
    


def main_loop():
    """
    Main game loop.
    """
    range_min = 0
    range_max = 100
    next_round = True
    number = 0
    
    while next_round:
        guesses = 1
        range_min, range_max = ask_for_range()
        number = generate_random_number(range_min, range_max)
        print(number)
        
        while (not guess_number(number)):
            guesses += 1
        
        print('You needed ', guesses, ' guesse(s).')
        next_round = ask_to_play_again()
                

main_loop()