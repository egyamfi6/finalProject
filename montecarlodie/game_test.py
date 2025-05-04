#Name: Emmanuel Gyamfi, ID: asw4uc
#GitHub:https://github.com/egyamfi6/
#game_test.py

from game import Game
import unittest
import numpy as np

from die import Die



# Create variable to capture results when necessary
results: str = ""

class GameTestSuite(unittest.TestCase):
  
    def test_1_check_is_container_list(self): 

        with self.assertRaises(TypeError):
        #Generate TypeError by passing a set object
            DieOne: np.array = np.array(['A', 'B', 'C', 'D', 'E', 'F'], dtype=str)

            dieOneInstance: Die = Die(DieOne)

            diceList: set = ((dieOneInstance))
            Game(diceList)

    def test_2_check_if_die_object(self): 

        with self.assertRaises(TypeError):
        #Generate TypeError by passing a set object
            DieOne: np.array = np.array(['A', 'B', 'C', 'D', 'E', 'F'], dtype=str)
            DieTwo: np.array = np.array(['A', 'B', 'C', 'D', 'E', 'F'], dtype=str)
            DieThree: np.array = np.array(['A', 'B', 'C', 'D', 'E', 'F'], dtype=str)

            diceList: set = [DieOne, DieTwo, DieThree]
            Game(diceList)


    def test_3_change_die_weight(self): 

    
        with self.assertRaises(ValueError):
            #Generate ValueError by passing an invalid option for narrow or wide
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
            myInstance.play(2)

            #The Results
            myInstance.playResults("x")

    
    def test_4_check_die_faces(self): 

    
        with self.assertRaises(ValueError):
            
            #Generate ValueError if all die have the same faces
            
            # The Die
            listDieOne: np.array = np.array(['A', 'B', 'C', 'D', 'E', 'F'], dtype=str)
            listDieTwo: np.array = np.array(['A', 'B', 'C', 'D', 'E', 'F'], dtype=str)
            listDieThree: np.array = np.array(['A', 'B', 'C', 'D', 'E', 'F'], dtype=str)
            listDieFour: np.array = np.array(['A', 'B'], dtype=str)

            dieOneInstance: Die = Die(listDieOne)
            dieTwoInstance: Die = Die(listDieTwo)
            dieThreeInstance: Die = Die(listDieThree)
            dieFourInstance: Die = Die(listDieFour)

            #Manage Die weighting
            dieOneInstance.change_die_weight('B', .40)
            dieTwoInstance.change_die_weight('B', .30)
            dieThreeInstance.change_die_weight('B', .20)

            diceList: list = [dieOneInstance, dieTwoInstance, dieThreeInstance, dieFourInstance]
            myInstance: Game = Game(diceList)

            #Let it roll!
            myInstance.play(2)

            #The Results
            myInstance.playResults("x")



    
if __name__ == '__main__':
    unittest.main(verbosity=3)
