import math
from colorama import init, Fore, Style
class MyOprations:
    #Triangle Types
    @staticmethod
    def TriangleAreaWithThreeSide(side1, side2, side3):
            if isinstance(side1,int) and isinstance(side2,int) and isinstance(side3,int): 
                if (side1 > side2 + side3) or (side2 > side1 + side3) or (side3 > side1 + side2): 
                  return "These Numbers won't make a triangle" 
                else:
                    perimeter = (side1 + side2 + side3)/2
                    return math.sqrt(perimeter * (perimeter - side1) * (perimeter - side2) * (perimeter - side3)) 
            else: 
                print("pls enter right value!")
                
    @staticmethod
    def TriangleAreaWithTwoSideAndAngle(side1, side2, angle):
        if isinstance(side1,int) and isinstance(side2,int) and isinstance(angle,int):
            return side1 * side2 * angle
        else: 
            print("pls enter right value!")
   
    @staticmethod
    def TriangleAreaUsingHeightAndBase(height, base):
        if isinstance(height,int) and isinstance(base,int):
            return height * base
        else: 
            print("pls enter right value!")
    #Triangle Types
    
    @staticmethod
    def RectangleArea(length, width):
        if isinstance(length,int) and isinstance(width,int):
            return length * width
        else: 
            print("pls enter right value!")
    @staticmethod
    def ProofOfGoldenRatio(x):
        if isinstance(x, int):
            return (math.sin(x)**2 + math.cos(x)**2)
        else: 
            print("pls enter right value!")

    @staticmethod
    def WordReverser(word: str):
        if isinstance(word, str):
            return word[::-1]
        else: 
            print("pls enter right value!")

    @staticmethod
    def WantToDoItAllAgain() -> bool:
        # برای تغییر رنگ کلمه یس
        print("pls enter ", Fore.GREEN, "yes ",Style.RESET_ALL ,"to ",Fore.GREEN , "contineu ", Style.RESET_ALL,
              "or anything else to ",Fore.RED ,"close the app:", Style.RESET_ALL )
        choose = input("pls enter what you want: ")
        match choose:
            case "yes":
               return True
            case _:
                return False

