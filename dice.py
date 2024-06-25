# Maftuna Zokirova

import random
from termcolor import colored


class Dice:
    def __init__(self) -> None:
        self.playAgain = 'Y'
        self.dieCounter = 0


    def DisplayStart(self) -> None:
        
        print(colored("Starting Craps Dice Rolling Simulation ", "light_magenta"))

    def GameLoop(self) -> None:
        while True:
            rolledSevens = 0
            rolledElevens = 0
            for i in range(100):
                self.dieCounter = self.Generate_Random_Number() + self.Generate_Random_Number()
                
                if self.dieCounter == 7:
                    rolledSevens += 1
                elif self.dieCounter == 11:
                    rolledElevens += 1

                    
            print("The play rolled " + str(rolledSevens) + "sevens and " + str(rolledElevens) + " elevens for a total of " + str( rolledSevens+ rolledElevens )+ " wins out of 100. ")
           
            # or print("The play rolled " ,  rolledSevens , "sevens and " , rolledElevens , " elevens for a total of ", rolledSevens , rolledElevens , " wins out of 100. "))
            user_input = input("Try again, Enter y for yes, n for no : ")
            print( user_input)
            
            if user_input != "y" :
                    break 
    
    def Generate_Random_Number(self) -> None:
        
        return random.randint(1, 7) 

    def Run(self) -> None:
        self.DisplayStart()
        self.GameLoop()
        
   