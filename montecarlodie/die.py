#Name: Emmanuel Gyamfi, ID: asw4uc
#GitHub:https://github.com/egyamfi6/finalProject
#die.py

#Import relevant libraries
import pandas as pd
import numpy as np
import random

#The die class
class Die:
    """
    -This is a class of a Die with 6 faces which can be rolled to select a face. 
    -The faces of the die are alphabetical letters or numeric(eg. A, B, C... or 1,2,3..) with equal weights that defaults to 1. 
    -This class contains a private dataframe that holds the faces and weights
     and has 4 methods including the intilializer, a method to change the weight of a single side of the die, 
    -a method that that rolls the die one or more times and a method that shows the current state of the die. 
   
    The methods in the class are:
        __init__(),
        change_die_weight(),
        roll_die(),
        die_state()
    """


    # The Initializer
    def __init__(self, dieParam: np.array) -> None: 
       
        """
        .This initializer takes a NumPy array of faces as an argument and throws a TypeError if not a NumPy array.
        .The array’s data type may be strings or numbers.
        .The array’s values must be distinct and if not, it raises a ValueError.
        .It internally initializes the weights to 1.0 for each face.
        .It saves both faces and weights in a private data frame with faces in the index.
        """
        
        if not type(dieParam) is np.ndarray:                          #checks to see if die is a Numpy array
            raise TypeError("The die must be of type NumPy Array!") # throws a TypeError if die is not a Numpy array

        if (len(np.unique(dieParam)) !=  len(dieParam)):                       #checks if die is unique 
            raise ValueError(f"The die must have distinct values! {dieParam}") # throws a valueError if die is not unique
        
        #Build Dynamic Index
        self.dieParam = dieParam
        self._privateDataFrame: pd.DataFrame = pd.DataFrame(self.dieParam, columns=['dieValue'], index=dieParam.tolist())

        for idx, row in self._privateDataFrame.iterrows():
            #Modify Face Value
            self._privateDataFrame.loc[idx] = 1.0
          
        
    #  method to change die weight
    def change_die_weight(self, face_name: str, new_weight: float) -> None:
        """
        .This method takes two arguments: the face value to be changed and the new weight.
        .Checks to see if the face passed is valid value, i.e. if it is in
        .the die array. If not, raises an `IndexError`.
        .Checks to see if the weight is a valid type, i.e. if it is numeric
        .(integer or float) or castable as numeric. If not, raises a `TypeError`.
        
        """
        if not (face_name in self._privateDataFrame.index):                     #checks if face name exist in die array
             raise IndexError(f"{face_name} does not exist in the die array: ") # raise IndexError if face name does not exist
        if not isinstance(new_weight, (int, float)):  
            raise TypeError(f"new weight request must be of type integer or float: {new_weight}") #checks if weight is numeric
        
        #Modify the requested die face
        self._privateDataFrame.loc[face_name] = new_weight
    
    
    # method to roll a die "roll_die"
    def roll_die(self, how_many_times: int = 1) -> list:
        """
        .This method takes a parameter of how many times the die is to be rolled; defaults to 1.
        .This is essentially a random sample with replacement, from the private die data frame, that applies the weights.
        .Returns a Python list of outcomes.
        .Does not store any results internally.
        """
        outcomes: list = list()
        facesList: list = self._privateDataFrame.index.to_list()
        weightsList: list = self._privateDataFrame['dieValue'].to_list()

        for roll in range(how_many_times):
            if ( (roll+1) == how_many_times):
                self._privateDataFrame.loc[facesList[0]:facesList[-1]] = 0.0
                outcomes.append(random.choices(facesList, weights=weightsList, k=1)[0])
                self._privateDataFrame.loc[outcomes[-1], 'dieValue'] = 1.0 
            else:
                outcomes.append(random.choices(facesList, weights=weightsList, k=1)[0])               
        return outcomes
    
    # a method to get the die_state
    def die_state(self) -> pd.DataFrame:
        """
        This method takes no arguments and returns a copy of the private data frame
        """
        return self._privateDataFrame
    
    
if __name__ == '__main__':

    # The Die
    dieArray: np.array = np.array(['A', 'B', 'C', 'D', 'E', 'F'], dtype=str)


    results: str = ""
    # Instantiate the Die class
    myInstance: Die = Die(dieArray)

    myInstance.change_die_weight('C', .30)

    print(f"Outcomes: \n{myInstance.roll_die(3)}")

    dieStateDataFrame: pd.DataFrame = myInstance.die_state()
    print(f"Die State: {dieStateDataFrame}")

    # The Coin (H-head of the coin, T-Tail of the coin)
    myCoin: np.array = np.array(['H', 'T'], dtype=str) 

    # Instantiate the Die class
    myCoinInstance: Die = Die(myCoin)
    
    myCoinInstance.change_die_weight('T', .30)

    print(myCoinInstance.roll_die(1))
    
    dieStateDataFrame: pd.DataFrame = myCoinInstance.die_state()
    print(f"Die State: {dieStateDataFrame}")


    