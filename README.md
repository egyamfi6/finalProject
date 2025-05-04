This is a Die game that micmics MonteCarlo simulation.

- **Source code:** https://github.com/egyamfi6/finalProject


General features of the game:

- Generate multifaceted dice with weights
- Alter die specific weights
- Die can be rolled one or more times per game
- Display game results to include jackpot results
- Computes how many times a given face is rolled in each event
- Computes the distinct combinations of faces rolled, along with their counts
- Computes the distinct permutations of faces rolled, along with their counts
- Computes how many times a given face is rolled in each event


Installation Requirements:

    At your system command prompt, enter pip install montecarlodie
        You should see the following results:
           
 -Preparing metadata (setup.py) ... done
 -Requirement already satisfied: Numpy in /apps/software/standard/core/jupyterlab/3.6.3-py3.11/lib/python3.11/site-packages (from MonteCarlo-Die- -Simulator==0.1.0) (1.24.4)
-Requirement already satisfied: Pandas in /apps/software/standard/core/jupyterlab/3.6.3-py3.11/lib/python3.11/site-packages (from MonteCarlo-Die----Simulator==0.1.0) (2.0.3)
-Requirement already satisfied: python-dateutil>=2.8.2 in /apps/software/standard/core/jupyterlab/3.6.3-py3.11/lib/python3.11/site-packages (from Pandas-->MonteCarlo-Die-Simulator==0.1.0) (2.8.2)
-Requirement already satisfied: pytz>=2020.1 in /apps/software/standard/core/jupyterlab/3.6.3-py3.11/lib/python3.11/site-packages (from Pandas->MonteCarlo-Die--Simulator==0.1.0) (2023.3)
-Requirement already satisfied: tzdata>=2022.1 in /apps/software/standard/core/jupyterlab/3.6.3-py3.11/lib/python3.11/site-packages (from Pandas->MonteCarlo--Die-Simulator==0.1.0) (2023.3)
-Requirement already satisfied: six>=1.5 in /apps/software/standard/core/jupyterlab/3.6.3-py3.11/lib/python3.11/site-packages (from python-dateutil>=2.8.2-->Pandas->MonteCarlo-Die-Simulator==0.1.0) (1.16.0)
-Installing collected packages: MonteCarlo-Die-Simulator
 -Running setup.py develop for MonteCarlo-Die-Simulator
-Successfully installed MonteCarlo-Die-Simulator-0.1.0
    -import required modules
       - For Example: Let's play a game where we create three die, give the three die the same weight
                       - and roll the three die ten (10) times.  You will be able to review the results and see if 
                       - you hit any jackpots!  You will also be able to see differing combinations and permutations
                       - of your die rolls.

        In a file called montecarloTest.py, use the following code sample

            from die import Die
            from analyzer import Analyzer
            from game import Game

            # The Die
            DieOne: np.array = np.array(['A', 'B', 'C', 'D', 'E', 'F'], dtype=str)
            DieTwo: np.array = np.array(['A', 'B', 'C', 'D', 'E', 'F'], dtype=str)
            DieThree: np.array = np.array(['A', 'B', 'C', 'D', 'E', 'F'], dtype=str)
            
            dieOneInstance: Die = Die(DieOne)
            dieTwoInstance: Die = Die(DieTwo)
            dieThreeInstance: Die = Die(DieThree)
            
            #Manage Die weighting
            dieOneInstance.change_die_weight('B', .20)
            dieTwoInstance.change_die_weight('B', .20)
            dieThreeInstance.change_die_weight('B', .20)

            diceList: list = [dieOneInstance, dieTwoInstance, dieThreeInstance]

            myInstance: Game = Game(diceList)

            #Let it roll!
            myInstance.play(10)

            myAnalyzerInstance: Analyzer = Analyzer(myInstance) 
            #myAnalyerErr: Analyzer = Analyzer(myErrorInstance)


API description
----------------------

## die.py
<code>
    class Die:
    """
    This is a class of a Die with 6 faces which can be rolled to select a face. 
    The faces of the die are alphabetical letters or numeric(eg. A, B, C... or 1,2,3..) with equal weights that defaults to 1. 
    This class contains a private dataframe that holds the faces and weights
    and has 4 methods including the intilializer, a method to change the weight of a single side of the die, 
    a method that that rolls the die one or more times and a method that shows the current state of the die. 
   
    Methods in the class are:
        __init__():
        change_die_weight() 
        roll_die()
        die_state()
    """

</code>

## game.py
<code>
class Game:
    """
    .This game class consists of rolling one or more similar dice (Die objects) one or more times.
    .Each die in a given game has the same number of sides and associated faces but may have its own weight.
    .Each game is initialized with a Python list that contains one or more dice.
    .Game objects have a behavior to play a game, i.e. to roll all of the dice a given number of times.
    .Game objects only keep the results of their most recent play.
    
    .The methods in ths class are:
        play() 
        playResults()
    """

          
</code>
## analyzer.py
<code>
 
class Analyzer:
    """
    .This Analyzer object takes the results of a single game and computes various descriptive statistics on them.
    .It has 4 methods. 

    The methods in the Analyzer class are:
        jackpots() 
        dieFaceCounter()
        dieComboCounter()
        diePermutationCounter()
    """

  
</code>

