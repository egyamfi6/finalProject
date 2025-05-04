#Name: Emmanuel Gyamfi, ID: asw4uc
#GitHub:https://github.com/egyamfi6/
#analyzer.py

#import relevant libraries
import pandas as pd
import numpy as np
from die import Die
from game import Game

# create the Analyzer class
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
    
    #the initializer 
    def __init__(self, gameParam: Game) -> None:
        """
        .This initializer takes a game object as its input parameter. 
        .It throws a ValueError if the passed value is not a Game object.
        .It does not return any value.
        
        """
        print(type(gameParam))
        if not type(gameParam) is Game:                                #checks if parameter passed is a game
            raise ValueError("The parameter must be of type Game!")  # raise a valueError if parameter is not a game
        self.gameParam = gameParam

    #the jackpot method
    def jackpots(self) -> int:
        
        """
        .This method computes how many times the game resulted in a jackpot.
        .A jackpot is a result in which all faces are the same, e.g. all ones for a six-sided die.
        .Returns an integer for the number of jackpots.
        """
        numberOfJackpots: int = 0

        #Load play Results
        diePlayResultsFrame: pd.DataFrame = self.gameParam.playResults("w")
        print(f"The DataFrame to examine for jackpot notifications: \n{diePlayResultsFrame}")

        #Check all rows in this dataframe
        rowsInDataFrame: int = len(diePlayResultsFrame)
       
        for rowIdx in range(1,rowsInDataFrame + 1):
            duplicates: pd.Series = diePlayResultsFrame.loc[rowIdx].duplicated()
            num_duplicates: np.int64 = duplicates.sum()
           
            if len(diePlayResultsFrame.loc[rowIdx]) == num_duplicates + 1:
                #We have a jackpot
                numberOfJackpots += 1
        
        return numberOfJackpots

    #the die face counter method
    def dieFaceCounter(self) -> pd.DataFrame:
        
        """
        .Computes how many times a given face is rolled in each event.
        .For example, if a roll of five dice has all sixes, then the counts for this roll would be  5
        .for the face value ‘6’ and  0 for the other faces.
        .It returns a data frame of results.
        .The data frame has an index of the roll number, face values as columns, 
        .and count values in the cells (i.e. it is in wide format).
        """

        df_ForFaceCounts: pd.DataFrame = self.gameParam.playResults("w").apply(pd.Series.value_counts, axis=1).fillna(0).astype(int)
        df_ForFaceCounts.index.name = "RollNum" #index of the game
        return df_ForFaceCounts                 #returns a data.frame


    # the combo counter method
    def dieComboCounter(self) -> pd.DataFrame:
        
        """
        .This method computes the distinct combinations of faces rolled, along with their counts.
        .The combinations are order-independent and may contain repetitions.
        .The method returns a dataframe of results,
        .The data frame should have a MultiIndex of distinct combinations and a column for the associated counts.
        """
         #Load play Results
        diePlayResultsFrame: pd.DataFrame = self.gameParam.playResults("w")
        dfMultiIndex: pd.DataFrame = diePlayResultsFrame.apply(lambda x: pd.Series(sorted(x)), 1).value_counts().to_frame('Frequency')
        dfMultiIndex.index.names = ["DieFace:"+str(i) for i in range(1, len(diePlayResultsFrame.columns.to_list())+1)]
        return dfMultiIndex
    

    # a method to count the die permutations
    def diePermutationCounter(self) -> pd.DataFrame:
        
        """
        .This method computes the distinct permutations of faces rolled, along with their counts.
        .Permutations are order-dependent and may contain repetitions.
        .It returns a data frame of results.
        .The data frame should have a MultiIndex of distinct permutations and a column for the associated counts.
        .Permutations are order-dependent and may contain repetitions.
        .The data frame should have a MultiIndex of distinct permutations and a column for the associated counts
        """

        #Load play Results
        diePlayResultsFrame: pd.DataFrame = self.gameParam.playResults("w")

        dfMultiIndex = diePlayResultsFrame.set_index(diePlayResultsFrame.columns.to_list(), append=True)
        dfMultiIdxPermCnt = dfMultiIndex.groupby(diePlayResultsFrame.columns.to_list()).size().to_frame("Frequency")
        return dfMultiIdxPermCnt

       

if __name__ == '__main__':

    # The Die (faces of the die are letters A through F)
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


    #diceList: list = [dieOneInstance, dieTwoInstance, dieThreeInstance, dieFourInstance]
    diceList: list = [dieOneInstance, dieTwoInstance, dieThreeInstance]

    #myErrorInstance: list = list(diceList)
    myInstance: Game = Game(diceList)

    #Let it roll!
    myInstance.play(10)
    
    print(type(myInstance))
    myAnalyzerInstance: Analyzer = Analyzer(myInstance) 
    #myAnalyerErr: Analyzer = Analyzer(myErrorInstance)

    #Jackot Information
    print(f"Did I hit any jackpots? \n{myAnalyzerInstance.jackpots()}")

    print(f"Play Results(Wide Format): \n{myAnalyzerInstance.dieFaceCounter()}")

    #print(f"Play Results(Narrow Format): \n{myInstance.playResults("x")}")

    print(f"Play Results(Wide Format): \n{myAnalyzerInstance.dieComboCounter()}")

    print(f"Play Results(Wide Format): \n{myAnalyzerInstance.diePermutationCounter()}")
