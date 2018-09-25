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
        self.num_players = np.nan
        self.h_dart = np.nan
        self.v_dart = np.nan
        self.s_dart = np.nan
        self.scoreb = pd.DataFrame()
        self.hit    = pd.DataFrame()
        
        self.n_hits = {15:0,
                       16:0,
                       17:0,
                       18:0,
                       19:0,
                       20:0,
                       25:0
                       }
    def init_scoreb_hit_b(self, n):
        hit_df = pd.DataFrame({'Player_1' : 0, 'Player_2' : 0}, index = [0] )
        n_players = int(n)
        if n_players < 2:
            print('Minumum number of players is 2 \n Try Again')
        
        elif n_players == 2:
            self.scoreb =  self.hit = hit_df
        else:
            for player in list(range(2, int(n_players)+1)):
                column_name = 'Player_'+str(player)
                hit_df.loc[:,column_name] = 0
                hit_df.loc[:,column_name] = hit_df[column_name].astype(np.int64)
            self.scoreb =  self.hit = hit_df
            
    def num_of_players(self):
        num_players = input("How many players:")
        self.init_scoreb_hit_b(num_players)
        
    def score_per_dart(self):
        self.h_dart = np.nan
        self.v_dart = np.nan
        self.s_dart = np.nan

        v_dart = np.nan
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
    
    def hits_update(self):
        v_dart = self.v_dart
        h_dart = self.h_dart
        hits_dict = self.n_hits 
        current_hits = hits_dict[v_dart]
        
        while current_hits < 3:
            h_dart = h_dart - 1
            current_hits = current_hits + 1
        
        self.hits_dict[v_dart] = current_hits
        self.v_dart = v_dart
        self.h_dart = h_dart
            
    def hits_score_per_turn(self):
        hits_dict = self.n_hits 
        if hits_dict[self.v_dart] >=3:
            print('{} is closed'.format(self.v_darth))
        hits  = 0
        score = 0
        for shot in list(range(1,4)):
            self.score_per_dart()
            score_ = self.s_dart
            score = score_ + score
        print('SCORE:', score)
            
       
        
    def print_numbers(self):
        return self.numbers

a = dart_score()
a.scoreb
a.num_of_players()
a.score_per_turn()

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
    


hits(2)
hits(5).info()
    

    
    
