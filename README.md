# Cricket Game Track App

## PURPOSE:
The purpose of this project is to build a tool to allow Cricket players to track the game and provide the score and the winner of the game. 

## DESCRIPTION:
The app follows the description and rules of the game, as provided in these two sites:
   - https://en.wikipedia.org/wiki/Cricket_(darts)
    
   - https://www.dartspiks.com/cricket.html
    
The features include:
   - Multiple players (minimum of 2).
   
   - Use the traditional 15 to 20 numbers and the bullseye. 
   
   - Handles multiple entries for each number, as well as missed targets, or other numbers in the board (all coded as zero).
          
          For example, 20 can be 20, twenty, twenty points, and veinte (twently in spahish)
   
   - Numbers are scored as single, double, and triple by multiplying the number and the number of hits (1, 2, or 3).
   
   - Bullseye is scored with 25 points as a single or 50 as a double. 
    
   - Continuos track of points (score) and number of hits.
   
   - Track the status of the numbers: Not open, open, and close. 
    
          Scores are added only if the number is open and only for the player that opened it. 
          Once the number is closed by another player, the score on that number is zero for all players. 
   
   - Track wich player Opens a number.
   
          Important in case of a tie in points - multiple ties are handle too
   
   - Determine when all numbers are closed and ends the game. 
   
   - Provide final score with tie break when scores are the same, using the number of numbers opened by the higher scoring players. 
   
  The app is built in *Python 3.6*, using *Syder 3.3.1* on *ANACONDA 1.9.2*. 
  
  Aside from the native functions, *pandas (0.23.0)* and *numpy (1.14.3)* were used. 
  
## RUNNING THE APP:

To run the app:
  - Clone/Download the repo
  
  - On a terminal go to the unzipped directory
  
  - Type: 
  
   `python cricket_dart_game.py` 
    
  - **OR**,  open the file in Spyder and run:
  
  `dart_game = play_dart()`
  
  `dart_game.play_darts()`
  
  -  **OR**, copy the code from the file into a Jupyter Notebook and run the commands above 
      
      This option may not display well
      
  - in all three cases, follow the prompts

**ENJOY**
  
   
   



