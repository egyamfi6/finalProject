#Name: Emmanuel Gyamfi, ID: asw4uc
#GitHub:https://github.com/egyamfi6/
#game.py


#import relevant libraries
import pandas as pd
import numpy as np
from die import Die

# create the Game class
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

    # create the initializer for the Game class
    def __init__(self, Dice: list[Die]) -> None: #change Dice to my own
        """
        .This initializes the Game class.
        .This Takes only one parameter, which is a list of already instantiated similar dice.
        .Does not check if the passed parameter is a list and does not check if the list is a die object.
        .Ouput: None- returns nothing. 
        """
       
        if not type(Dice) is list:
            raise TypeError("The container for the dice must be of type list!") 

        #List items must be Die Objects
        for item in Dice:
            if not isinstance(item, Die):
                raise TypeError(f"List element: {item} is not of type {Die.__name__} !")
        
        self.Dice = Dice

        #Use this empty dictionay object for private pandas dataFrame
        emptyDict = {'RollNum': [],
        'DieId': [],
        'DieValue': []}

        self._privateGameDataFrame: pd.DataFrame = pd.DataFrame(emptyDict)

        
        #All Die objects in list must have the same number of faces
        checkCoinFaces: bool = all(len(x.die_state()) == 2 for x in Dice)   #Two Face Coin
        checkDieFaces: bool = all(len(x.die_state()) == 6 for x in Dice)   #Six Face Die
        checkAlphaDieFaces: bool = all(len(x.die_state()) == 26 for x in Dice)   #Alphabet Face Die

        #Raise error if die objects do not have the same number of faces
        if checkCoinFaces == False and checkDieFaces == False and checkAlphaDieFaces == False:
            raise ValueError(f"All Die objects in list must have the same number of faces!")
        
    
    def play(self, how_many_rolls: int) -> None:
        
        """
        .This method takes an integer parameter to specify how many times the dice should be rolled.
        .It saves the result of the play to a private data frame.
        .The data frame should be in wide format, i.e. have the roll number as a named index, 
        .columns for each die number (using its list index as the column name), and the face rolled in that instance in each cell.
        .Returns nothing
        """

        print(f"Entering method play: Number of requested rolls ({how_many_rolls})\n") #will delete this

        print(f"Number of Die in play: {len(self.Dice)}")                   #will delete this


        allDieRollResults: list = []

        dieID: int = 1
        for item in self.Dice:
            dieRoll: list = item.roll_die(how_many_rolls)
            dieRollResults: list = [(i + 1, dieID, dieRoll[i]) for i in range(len(dieRoll))]
            allDieRollResults = allDieRollResults + dieRollResults
            dieID += 1

        #Save Results to private Dataframe with newly generated list
        self._privateGameDataFrame = pd.DataFrame(allDieRollResults, columns=['RollNum', 'DieId', 'DieValue'])



    def playResults(self, df_frame_type: str = 'w') -> pd.DataFrame:
        
        """
        
        .This method just returns a copy of the private play data frame to the user.
        .Takes a parameter to return the data frame in narrow or wide form which defaults to wide form.
        .The narrow form will have a MultiIndex, comprising the roll number and the die number (in that order), 
          and a single column with the outcomes (i.e. the face rolled).
        .This method raises a ValueError if the user passes an invalid option for narrow or wide.
        """

        if (df_frame_type != "w") and (df_frame_type != "n"):
            raise ValueError(f"invalid option for (n)arrow or (w)ide: {df_frame_type}\n")

        if df_frame_type == "w":
            return self._privateGameDataFrame.pivot(index='RollNum', columns='DieId', values='DieValue')
        elif df_frame_type == "n":
            return self._privateGameDataFrame.set_index(['RollNum', 'DieId'])
            

if __name__ == '__main__':

    # The Die
    listDieOne: np.array = np.array(['A', 'B', 'C', 'D', 'E', 'F'], dtype=str)
    listDieTwo: np.array = np.array(['A', 'B', 'C', 'D', 'E', 'F'], dtype=str)
    listDieThree: np.array = np.array(['A', 'B', 'C', 'D', 'E', 'F'], dtype=str)
   

    dieOneInstance: Die = Die(listDieOne)
    dieTwoInstance: Die = Die(listDieTwo)
    dieThreeInstance: Die = Die(listDieThree)


    #Manage Die weighting
    dieOneInstance.change_die_weight('B', .40)
    dieTwoInstance.change_die_weight('B', .30)
    dieThreeInstance.change_die_weight('B', .20)


    diceList: list = [dieOneInstance, dieTwoInstance, dieThreeInstance]
    myInstance: Game = Game(diceList)

    #Let it roll!
    myInstance.play(3)

    #The Results
    print(f"Play Results(Wide Format): \n{myInstance.playResults()}")
