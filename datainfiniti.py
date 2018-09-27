#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 18:11:55 2018

@author: jpinzon
"""
import numpy as np
import pandas as pd
class dart_score():
    def __init__(self):
        self.numbers = [25, 20, 19, 18, 17, 16, 15, 0]
        self.player_number = np.nan
        self.h_dart = np.nan
        self.v_dart = np.nan
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
    def init_scoreb_hit_b(self, number):
        hit_df1 = pd.DataFrame({'Player_1': 0, 'Player_2': 0}, index = [0] )
        n_players = int(number)
        if n_players < 2:
            print('Minumum number of players is 2 \n Try Again')
        elif n_players == 2:
            score_df =  hit_df = hit_df1
        else:
            for player in list(range(2, int(n_players) + 1)):
                column_name = 'Player_' + str(player)
                hit_df1.loc[:,column_name] = 0
                hit_df1.loc[:,column_name] = hit_df1[column_name].astype(np.int64)
                score_df = hit_df = hit_df1
        #score_df.loc[:,'SCORE'] = 'SCORE'
        #score_df = score_df.set_index('SCORE')
        score_df.index.name = 'SCORES'
        self.score_df = score_df
        for number in self.numbers[0:7]:
            
            s2 = pd.Series([0] * n_players, index = hit_df.columns, name = number)
            hit_df = hit_df.append(s2)
            hit_df.index.name = 'NUMBER'
        self.hit_df = hit_df.drop(0, 0).sort_index()
               
    def num_of_players(self):
        self.player_number = input("How many players:")
        self.init_scoreb_hit_b(self.player_number)
        
    def score_per_turn(self):
        self.h_dart = v_dart = np.nan
        self.v_dart = h_dart = np.nan
        
        while np.isnan(v_dart):
            # Asking for the number hit in the turn
            v_dart = input('Number 15-20 and Bullseye (B or 25). Missed/Other number = 0):')
            if v_dart.upper() == 'B':
                v_dart = 25
            else:
                v_dart = int(v_dart)
            if v_dart in self.numbers:
                print('Thanks, Value accepted')
            else:
                print('#### Check the values and try again ####')
                v_dart = np.nan
        if v_dart != 0:
            h_dart = np.nan
        else:
            h_dart = 0
        while np.isnan(h_dart):
            if v_dart == 25:
                msg = 'Enter the appropiate value:\n 1. Single \n 2. Double '
                value_l = [1, 2]
            else:
                msg = 'Enter the appropiate value:\n 1. Single \n 2. Double \n 3. Triple'
                value_l = [1, 2, 3]
            print(msg)
            h_dart = int(input('Score:'))
            if h_dart in value_l:
                print('\nThanks score been calculated')
            else: 
                print('#### Check the values and try again ####')
                h_dart = np.nan
        self.h_dart = h_dart
        self.v_dart = v_dart
        self.hits_update()
    
    def hits_update(self):
        player_number  = self.player_number
        v_dart   = self.v_dart
        h_dart   = self.h_dart
        n_hits   = self.n_hits 
        score_df = self.score_df
        hit_df   = self.hit_df
        
        if v_dart ==0:
            self.score_df = score_df
            self.hit_df = hit_df
        
        else:
            # Check number status:
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
                    
            open_player = n_hits[v_dart]['player']
            if (n_status == 1) & (player_number == open_player):
                score = v_dart * h_dart
            if (n_status == 1) & (player_number != open_player):
                score = 0
                player_hits = int(hit_df[player_number].loc[[v_dart]])
                if player_hits < 3:
                    player_hits = player_hits + h_dart
                    hit_df[player_number].loc[[v_dart]] = player_hits
                    h_dart = h_dart - player_hits
                
                if player_hits >= 3:
                    hit_df[player_number].loc[[v_dart]] = 3
                    n_hits[v_dart]['status'] = 2
            if n_status == 2:
                score = 0
            score_df[player_number].loc[[0]] = score_df[player_number].loc[[0]] + score
            self.score_df = score_df
            self.hit_df = hit_df
            print(hit_df)
            print(score_df)
    
    def record_play(self):
        for play in [1, 2, 3]:
            print('Now playing: {}'.format(self.player_number))
            print('Turn',format(play))
            self.score_per_turn()
        
    def play_darts(self):
        player = self.player_number
        if np.isnan(player):
            self.num_of_players()
            player = players = self.player_number
        
        while pd.DataFrame(data = self.n_hits).T.status.sum() < 14:
            if (np.isnan(int(player)) == False):
                for player in list(range(1, 1 + int(players))):
                    self.player_number = 'Player_' + str(player)
                    self.record_play()
                    print('GOOD PLAY!!! KEEP THE HARD WORK!!!')
                    print('##############################################')

        print('##############################################')
        print('################# GAME OVER ##################')
        final_score = self.score_df
        final_score.loc[:,'SCORE'] = 'SCORE'
        final_score = final_score.set_index('SCORE')
        final_score.index.name = ''
        winner = final_score.idxmax(axis=1)[0]
        max_score = final_score.max(axis=1)[0]
        
        print('##############################################')
        print('##############################################')

        print('############# FINAL SCORE TABLE ##############\n', 
              final_score,
              '\n############# FINAL SCORE TABLE ##############')

        print('##############################################')

        print('THE WINNER IS {}\nWITH {} POINTS'.format(winner, max_score))
                
        print('##############################################')
        print('##############################################')

dart_score().play_darts()
