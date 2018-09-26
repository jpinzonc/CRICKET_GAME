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
        self.numbers = [25, 20, 19, 18, 17, 16, 15, 0]# Using 50 as bullseye
        self.player_number = np.nan
        self.num_players = np.nan
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
    def init_scoreb_hit_b(self, n):
        hit_df = pd.DataFrame({'Player_1' : 0, 'Player_2' : 0}, index = [0] )
        n_players = int(n)
        if n_players < 2:
            print('Minumum number of players is 2 \n Try Again')
        elif n_players == 2:
            score_df =  hit_df = hit_df
        else:
            for player in list(range(2, int(n_players)+1)):
                column_name = 'Player_'+str(player)
                hit_df.loc[:,column_name] = 0
                hit_df.loc[:,column_name] = hit_df[column_name].astype(np.int64)
            score_df = hit_df = hit_df
        score_df.index.name = 'SCORES'
        self.score_df = score_df
        for number in self.numbers[0:7]:
            s2 = pd.Series([0] * n_players, index = hit_df.columns, name = number)
            hit_df = hit_df.append(s2)
            hit_df.index.name = 'NUMBER'
        self.hit_df = hit_df.drop(0,0).sort_index()
               
    def num_of_players(self):
        self.num_players = input("How many players:")
        self.init_scoreb_hit_b(self.num_players)
        
    def score_per_turn(self):
        self.h_dart = v_dart = np.nan
        self.v_dart = h_dart = np.nan
        print(v_dart, h_dart, 'ACA')
        while np.isnan(v_dart):
            # Asking for the number hit in the turn
            v_dart = input('Number (Bullseye = B or 25. Missed = 0):')
            if v_dart.upper() == 'B':
                v_dart = 25
            else:
                v_dart = int(v_dart)
            
            if v_dart in self.numbers:
                print('Thanks, Score being calculated')
            else:
                print('#### Check the values and try again ####')
                v_dart = np.nan
        if v_dart !=0:
            h_dart = np.nan
        else:
            h_dart = 0
        while np.isnan(h_dart):
            if v_dart == 25:
                msg = 'Enter the appropiate value:\n 1. Single \n 2. Double '
                value_l = [1,2]
            else:
                msg = 'Enter the appropiate value:\n 1. Single \n 2. Double \n 3. Triple'
                value_l = [1,2,3]
            print(msg)
            h_dart = int(input('Score:'))
            if h_dart in value_l:
                print('Thanks score been calculated')
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
        print(v_dart, h_dart)
        
        # Check number status:
        n_status = n_hits[v_dart]['status']
        print(n_status, 'STATIS')
        if n_status == 0:
            score = 0
            #check hits
            current_hits = int(hit_df[player_number].loc[[v_dart]])
            print(current_hits, 'q')
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
                    
            print(current_hits, 'q2')
            if current_hits >= 3:
                hit_df[player_number].loc[[v_dart]] = 3
                n_hits[v_dart]['status'] = 1
                n_hits[v_dart]['player'] = player_number
                n_status = n_hits[v_dart]['status']
                
        print(n_status, 'SATUS1')
        open_player = n_hits[v_dart]['player']
        print(open_player, h_dart)
        if (n_status == 1) & (player_number == open_player):
            score = v_dart * h_dart
        if (n_status == 1) & (player_number != open_player):
            score = 0
            player_hits = int(hit_df[player_number].loc[[v_dart]])
            print(player_hits, 'q3')
            if player_hits < 3:
                player_hits = player_hits + h_dart
                hit_df[player_number].loc[[v_dart]] = player_hits
                h_dart = h_dart - player_hits
                    
                print(player_hits, 'q4')
                if player_hits >= 3:
                    hit_df[player_number].loc[[v_dart]] = 3
                    n_hits[v_dart]['status'] = 2
        if n_status == 2:
            score = 0
        print(score)
        score_df[player_number].loc[[0]] = score_df[player_number].loc[[0]] + score
        print(hit_df)
        self.score_df = score_df
        self.hit_df = hit_df
        print(score_df)

    
    def record_play(self):
        player_number = input('Enter player number:')
        self.player_number = 'Player_'+str(player_number)
        for play in [1,2,3]:
            print('Turn',format(play))
            self.score_per_turn()

        
    def play(self):
        if np.isnan(self.player_number):
            print ('Players')
        else:
            print('GOOD')

a = dart_score()
a.play()
a.num_of_players()

a.n_hits
a.hit_df
a.score_df.T
a.record_play()


b = a.n_hits
b[15]=2
h = 2
num = b[15]
print(num)
if num < 3:
    num1 = 3 - num
    print(num1)
    h1 = h - num1
    b[15] = num + num1
print(b[15], h1)  

a = dart_score()
b = a.n_hits
b[15]
current_hits = b[15]
print(b[15])
number = 4
while current_hits < 3:
    number = number -1
    current_hits = current_hits + 1
print(number, current_hits)
 
c = a.hit_df
numbers = [25, 20, 19, 18, 17, 16, 15]# Using 50 as bullseye
for number in numbers:
    s2 = pd.Series([0] * 7, index=c.columns, name = number)
    c = c.append(s2)
c  
   
for col in c.columns:
    for number in numbers:
        print(col, number)
    print(col)
    c.loc[:,col] = 
    
s2 = pd.Series([0] * 7, index = c.columns)

result = c.append(s2, ignore_index = True)

a.numbers[0:7]
c.sort_index()

c['Player_1'].loc[[16]]
    

a.hit_df['Player_1'].loc[[16]]  == 0
    
