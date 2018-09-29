#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 18:11:55 2018
App designed to keep track of scores in the Dart Game Cricket
@author: Jorge Pinzón
"""
import numpy as np
import pandas as pd
class play_dart():
    '''
    play_dart is a class function that tracks the score of a Cricket Dart Game
    This class follows the rules described in wikipedia (https://en.wikipedia.org/wiki/Cricket_(darts))
    Can accept any number of players higher or equal to 2. 
    Uses the traditional numbers 15 - 20 and the Bullseye and records single, double, and triple points. 
    If can take several inputs for each number, including numbers, strings, and spanish.
    '''
    def __init__(self):
        # Set variables for the game 
        ## Numbers used in traditional Cricket (Darts)
        self.numbers = [25, 20, 19, 18, 17, 16, 15, 0] 
        ## Different acceptable numbers input
        self.numbers_dict = {15: [15, '15', 'fifteen', 'fifteen points', 'quince'],
                             16: [16, '16', 'sixteen', 'sixteen points', 'dieciseis'],
                             17: [17, '17', 'seventeen', 'seventeen points', 'diecisiete'],
                             18: [18, '18', 'eigthteen', 'eigthteen points', 'dieciocho'],
                             19: [19, '19', 'nineteen', 'nineteen points', 'diecinueve'],
                             20: [20, '20', 'twenty', 'twenty points', 'veinte'],
                             25: [25, '25', '25', 'bullseye', 'b', 'diana'],
                              0: [ 0,  '0', 'missing', 'no points', 'out', 'zero', 'no puntuación']}
        ## Records number of players
        self.player_number = np.nan
        ## Number and points for each turn 
        self.h_dart = np.nan
        self.v_dart = np.nan
        ## Records total points (score_df), hits (hit_df), 
        ## and status of the numbers (n_hits)
        self.score_df = pd.DataFrame()
        self.hit_df   = pd.DataFrame()
        self.n_hits = {15:{'status':0,'player':0},
                       16:{'status':0,'player':0},
                       17:{'status':0,'player':0},
                       18:{'status':0,'player':0},
                       19:{'status':0,'player':0},
                       20:{'status':0,'player':0},
                       25:{'status':0,'player':0}
                       }

    def init_scoreb_hit_b(self):
        '''
        Asks for the number of players in the game and generates the initial 
        score and hit tables depending for the number of players.
        '''
        self.player_number = self.num_players = input("How many players:")    
        # Template DF
        hit_df1 = pd.DataFrame({'Player_1': 0, 'Player_2': 0}, index = [0] )
        n_players = int(self.player_number)
        # Check number of players less than 2
        if n_players < 2:
            print('### Minumum number of players is 2 ###\n### Try Again ###')
        # for number of payers = 2, the template DF is used
        elif n_players == 2:
            score_df =  hit_df = hit_df1
        # adjust the template DF to the correct nnumber of players
        else:
            for player in list(range(2, int(n_players) + 1)):
                column_name = 'Player_' + str(player)
                hit_df1.loc[:,column_name] = 0
                hit_df1.loc[:,column_name] = hit_df1[column_name].astype(np.int64)
                score_df = hit_df = hit_df1
        # DF to track scores
        score_df.name = 'SCORE'
        self.score_df = score_df
        for number in self.numbers[0:7]:
            s2 = pd.Series([0] * n_players, index = hit_df.columns, name = number)
            hit_df = hit_df.append(s2)
            hit_df.index.name = 'NUMBER'
        # DF to track numbers as not played 0, open 1, and closed 2 and the 
        # player that openned it  
        self.hit_df = hit_df.drop(0, 0).sort_index()
               
    def score_per_turn(self):
        '''
        Function to calculate each turn score.
        With that score, it triggers the hits_update function
        '''
        self.h_dart = v_dart = np.nan
        self.v_dart = h_dart = np.nan
        while np.isnan(v_dart):
            # Asking for the number hit in the turn
            val_input = input('Enter the Number (numbers of letters - for missed enter missing or 0):')
            v_dart = next((k for k, v in self.numbers_dict.items() if val_input.lower() in v), 'Notfound')
            if v_dart == 'Notfound':
                print('#### Check the values and try again ####')
                v_dart = np.nan
            else:
                print('Thanks, Value accepted')
        if v_dart in self.numbers[0:7]:
            h_dart = np.nan
        else:
            h_dart = 0
        while np.isnan(h_dart):
            if v_dart == 25:
                msg = 'Enter the points for Number:\n 1. Single \n 2. Double'
                value_l = [1, 2]
            else:
                msg = 'Enter the points for Number:\n 1. Single \n 2. Double \n 3. Triple'
                value_l = [1, 2, 3]
            print(msg)
            h_dart = int(input('Points:'))
            if h_dart in value_l:
                print('\nThanks score been calculated')
            else: 
                print('#### Check the values and try again ####')
                h_dart = np.nan
        self.h_dart = h_dart
        self.v_dart = v_dart
        self.hits_update()
    
    def hits_update(self):
        '''
        This function uses the score for each turn and uptades:
            score_df -- Game Score
            hit_df   -- Hits table
            n_hit    -- Number status
        '''
        player_number  = self.player_number
        v_dart   = self.v_dart
        h_dart   = self.h_dart
        n_hits   = self.n_hits 
        score_df = self.score_df
        hit_df   = self.hit_df
        # In case os missing/not playing numbers
        if v_dart == 0:
            self.score_df = score_df
            self.hit_df = hit_df
        else:
            # Check number status:
            ## if status is empty
            n_status = n_hits[v_dart]['status']
            if n_status == 0:
                score = 0
                #check hits
                current_hits = int(hit_df[player_number].loc[[v_dart]])
                if current_hits == 0:
                    current_hits = current_hits + h_dart
                    h_dart = 0
                elif current_hits < 3:
                    need = 3 - current_hits
                    if h_dart <= need:
                        current_hits = current_hits + need
                        h_dart = 0
                    if h_dart > need:
                        h_dart = h_dart - need
                        current_hits = current_hits + need
                hit_df[player_number].loc[[v_dart]] = current_hits
                if current_hits >= 3:
                    hit_df[player_number].loc[[v_dart]] = 3
                    n_hits[v_dart]['status'] = 1
                    n_hits[v_dart]['player'] = player_number
                    n_status = n_hits[v_dart]['status']
            ## if not       
            open_player = n_hits[v_dart]['player']
            if (n_status == 1) & (player_number == open_player):
                score = v_dart * h_dart
            elif (n_status == 1) & (player_number != open_player):
                score = 0
                player_hits = int(hit_df[player_number].loc[[v_dart]])
                if player_hits < 3:
                    player_hits = player_hits + h_dart
                    hit_df[player_number].loc[[v_dart]] = player_hits
                    h_dart = h_dart - player_hits
                if player_hits >= 3:
                    hit_df[player_number].loc[[v_dart]] = 3
                    n_hits[v_dart]['status'] = 2
            ## if closed
            elif (n_status == 2) & (self.hit_df.loc[v_dart].sum() < (3 * int(self.num_players))):
                score = 0
                player_hits = int(hit_df[player_number].loc[[v_dart]])
                if player_hits < 3:
                    player_hits = player_hits + h_dart
                    hit_df[player_number].loc[[v_dart]] = player_hits
                if player_hits >= 3:
                    hit_df[player_number].loc[[v_dart]] = 3
                    score = 0
            elif (n_status == 2) & (self.hit_df.loc[v_dart].sum() >= (3 * int(self.num_players))):
                score = 0
            score_df[player_number].loc[[0]] = score_df[player_number].loc[[0]] + score
            self.score_df = score_df
            self.hit_df = hit_df
        # Print the current score and hits
        print(hit_df)
        print(score_df)
    
    def record_play(self):
        '''
        Runs each turn for each player
        '''
        for play in [1, 2, 3]:
            print('Now playing: {}'.format(self.player_number))
            print('Turn',format(play))
            self.score_per_turn()
        
    def play_darts(self):
        '''
        Main function, starts the game, runs the turns, 
        keeps track of the status of the numbers, 
        stops the game when all numbers have a closed (2) status, and
        generates the score and final result. 
        '''
        # Check if player number is null to start the game
        player = self.player_number
        if np.isnan(player):
            self.init_scoreb_hit_b()
            player = players = self.player_number
        # If player number is not null plays the game
        if (np.isnan(int(player)) == False):
            while pd.DataFrame(data = self.n_hits).T.status.sum() < 14:
                for player in list(range(1, 1 + int(players))):
                    self.player_number = 'Player_' + str(player)
                    self.record_play()
                    # Checking there is a number still open
                    if pd.DataFrame(data = self.n_hits).T.status.sum() == 14:
                        break
                    print('###############################################')
                    print('##### GOOD PLAY!!!  KEEP THE HARD WORK!!! #####')
                    print('###############################################')
                          
        print('###############################################')
        print('################# GAME OVER ###################')
        # Checking the score
        final_score = self.score_df
        final_score.loc[:,'SCORE'] = 'SCORE'
        final_score = final_score.set_index('SCORE')
        final_score.index.name = ''
        # Checking for ties and deciding the winner
        max_count = final_score.T['SCORE'].value_counts().iloc[:1].index[0]
        if max_count == final_score.max(1)[0]:
            print('Points tied - deciding winner on numbers closed')
            winner = pd.DataFrame(data = self.n_hits).T.player.value_counts().idxmax(axis = 0)
            max_score = final_score.max(axis=1)[0]   
        else:    
            winner = final_score.idxmax(axis=1)[0]
            max_score = final_score.max(axis=1)[0]
        print('###############################################')
        print('###############################################')
        print('############# FINAL SCORE TABLE ###############\n{}'\
              '\n############# FINAL SCORE TABLE ###############'.format(final_score))
        print('###############################################')
        print('########## THE WINNER IS {} ##########\n##########     WITH {} POINTS     ##########'.format(winner, max_score))
        print('###############################################')
        print('###############################################')

dart_game = play_dart()

dart_game.play_darts()
