#Name: Emmanuel Gyamfi, ID: asw4uc
#GitHub:https://github.com/egyamfi6/
#analyzer_test.py

#import relevant libraries
from analyzer import Analyzer
import unittest
import numpy as np

from die import Die
from game import Game



# Create variable to capture results when necessary
results: str = ""

class AnalyzeTestSuite(unittest.TestCase):
  
    def test_1_check_is_game_object(self): 

        with self.assertRaises(ValueError):
            #Generate ValueError by passing an invalid game object
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

            myErrorInstance: list = list(diceList)
            
            myAnalyerErr: Analyzer = Analyzer(myErrorInstance)

                    

if __name__ == '__main__':
    unittest.main(verbosity=3)
