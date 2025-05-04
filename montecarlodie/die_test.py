#Name: Emmanuel Gyamfi, ID: asw4uc
#GitHub:https://github.com/egyamfi6/finalProject
#die_test.py

#import relevant libraries
from die import Die
import unittest
import numpy as np


# Create global variable to capture results when necessary
results: str = ""

class DieTestSuite(unittest.TestCase):
    def test_1_check_distinct_die_weights(self): 
        with self.assertRaises(ValueError):
            #Generate ValueError by passing numpy array argument that contains a set of non-distinct items  
            dieArray: np.array = np.array(['A', 'A', 'C', 'D', 'E', 'F'], dtype=str)
            myDieInstance: Die = Die(dieArray)

    def test_2_change_die_weight(self): 
        
        with self.assertRaises(IndexError):
            dieArray: np.array = np.array(['A', 'B', 'C', 'D', 'E', 'F'], dtype=str)
            myDieInstance: Die = Die(dieArray)
            #Generate IndexError by passing a non-existent face_name argument
            myDieInstance.change_die_weight('G', .30) # G face does not exist and should trigger an error

    def test_3_change_die_weight(self): 
        with self.assertRaises(TypeError):
            dieArray: np.array = np.array(['A', 'B', 'C', 'D', 'E', 'F'], dtype=str)
            myDieInstance: Die = Die(dieArray)
            #Generate TypeError by passing new weight argument as a string
            myDieInstance.change_die_weight('C', '30')  #since weight is not of type float, this should trigger an error


    
    
        

  
        
if __name__ == '__main__':
    unittest.main(verbosity=3)
