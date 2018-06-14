#! /usr/bin/env python

# Simple python app built using testing based on The Python Book page 33
# Write outline program remembering that you are going to have to test
# So any functions that are used need to be pure, inputs, outputs and no side effects.

import random
import time
# 1.Models

# represent choices as numbers (constants)
rock = 1
paper = 2
scissors = 3

# use hashes for names of choices and rules
names = { rock: "Rock", paper: "Paper", scissors: "Scissors" } # constants
rules = { rock: scissors, paper: rock, scissors: paper } # constants

# 2. state is the values of models and variables in functions and can be tested

# 3. behaviour is what happens in functions and can be tested

def game(move_function, result_function, play_again_function, score):
    player = move_function()
    computer = random.randint(1,3)
    score = result_function(player, computer, score) if player in (1,2,3) else score
    return play_again_function(), score

def scores(score):
    print "HIGH SCORES"
    print "Player:",score[0]
    print "Computer:",score[1]

def move():
    while True:
        print
        player = raw_input("Rock = 1\nPaper = 2\nScissors = 3\nMake a move: ")
        try:
            player = int(player)
            if player in (1,2,3):
                return player
        except ValueError:
            pass
        print "Oops! I didn't understand that."
        return player


def result(player, computer, score):
    if player == computer:
        print "Tie game."
    else:
        if rules[player] == computer:
            score[0] += 1
            print "Your victory has been assured."
        else:
            score[1] += 1
            print "Computer wins ha ha. Na na na na na you lose."
    return score

def play_again():
    answer = raw_input("Would you like to play again? y/n: ")
    if answer in ("y", "yes", "Yes", "yep"):
        return answer
    else:
        print "Bye. Thank you for playing"

def print_welcome(greeting):
    print greeting

def start(greeting, print_welcome, game_function, scores_function, score):
    print_welcome(greeting)
    while True:
        carry_on, score = game_function(move, result, play_again, score)
        if not carry_on:
            scores_function(score)
            break

# basic program
if __name__ == '__main__':
    # outer functionality welcomes to game, plays game and then gives scores
    start("Let's play a game of Rock, Paper, Scissors.", print_welcome, game, scores, [0,0])
