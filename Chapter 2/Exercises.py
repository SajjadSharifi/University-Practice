'''
بسم الله الرحمن الرحیم
محمد سجاد شریفی پناه

**Part 1.**  The volume of a sphere with radius $r$ is $\frac{4}{3} \pi r^3$.
What is the volume of a sphere with radius 5? Start with a variable named `radius` and then assign the result to a variable named `volume`. 
Display the result.Add comments to indicate that `radius` is in centimeters and `volume` in cubic centimeters.

**Part 2.** A rule of trigonometry says that for any value of $x$, $(\cos x)^2 + (\sin x)^2 = 1$. Let's see if it's true for a specific value of $x$ like 42.
Create a variable named `x` with this value.
Then use `math.cos` and `math.sin` to compute the sine and cosine of $x$, and the sum of their squared.
The result should be close to 1. It might not be exactly 1 because floating-point arithmetic is not exact---it is only approximately correct.

**Part 3.** In addition to `pi`, the other variable defined in the `math` module is `e`, which represents the base of the natural logarithm, written in math notation as $e$.
If you are not familiar with this value, ask a virtual assistant "What is `math.e`?" Now let's compute $e^2$ three ways:
* Use `math.e` and the exponentiation operator (`**`).
* Use `math.pow` to raise `math.e` to the power `2`.
* Use `math.exp`, which takes as an argument a value, $x$, and computes $e^x$.
You might notice that the last result is slightly different from the other two.
See if you can find out which is correct.

''' 
import math as Math

def part1 (radius: int): # بر حسب سانتی متر
    if isinstance(radius , int):
        print("part 1: ", "volume of sqhere ")
        print( (4/3) * Math.pi * radius) # جواب بر حسب سانتی متر مکعب خواهد بود 
    else:
        print("Pls enter a valid radius number !!")

def part2 (value : int):
    if isinstance(value, int):
        print("proof of golden ratio")
        print( Math.sin(value)**2 + Math.cos(value)**2)
    else:
        print("pls enter a valid number")

def part3(howToDoIt :int):
    if isinstance(howToDoIt,int):
        if(howToDoIt ==1):
            print("way 1: simple power operation")
            print(Math.e ** 2)
        elif(howToDoIt ==2):
            print("way 2: pow method")
            print(Math.pow(Math.e,2))
        elif(howToDoIt == 3):
            print("way 3: exp method")
            print(Math.exp(2))
        else:
            print("pls enter a number from 1 to 3")

ProgramRuningStateMent = 1
waySelected =0

while ProgramRuningStateMent == 1:
    # while started
    
    print("wellcome to chapter 2 practice")
    print("pls enter the excersise number to go throw it's operation")
    print("pls select the part's number [1 or 2 or 3]")

    selectedPart = int(input())

    if selectedPart > 3 or selectedPart < 1:
        print("pls enter valid number")
        continue
    else:
        if(selectedPart == 1):
            part1(5)
        elif(selectedPart == 2):
            part2(42)
        elif(selectedPart == 3):
            print("pls select the way of doing the operation by selectin 1 to 3")
            waySelected = int(input())
            part3(waySelected)
        else:
            print("pls enter valid number","\n")
    # end of else

    print("if you wnat to continue pls enter number 1, anything else will close the operation")
    ProgramRuningStateMent = int(input())
    if(ProgramRuningStateMent == 1):
         continue
    else:
         break         
# end of while       

print("\n", "thanks for chosing us", "\n", "GoodBye and GoodLuck") 