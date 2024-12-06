# بسم الله الرحمن الرحیم
# محمد سجاد شریفی پناه
# exercise 1: make a triangle 
def triangle(pointStyle: str, height: int):
    if isinstance(pointStyle,str) and isinstance(height, int): 
        for i in range(height + 1):
            print(pointStyle * i)
    print()

# میخوام یک مستطیل بسازم
# با روش دستی :-)
def rectangle (rectangleStyle: str, height: int, length: int):
    if isinstance(rectangleStyle, str) and isinstance(height, int) and isinstance(length, int):
        for rectangleHeight in range(height):
            if rectangleHeight != 0:
                print()
            print(rectangleStyle, end= "")
            for rectangleLength in range(length):
                print(rectangleStyle, end="")

# من از 2 روش نوشتن معکوس رو مینویسم
def reversPrinter (numberOfPrinting: int, text: str):
    if isinstance(numberOfPrinting, int) and isinstance(text, str):
        for i in range(numberOfPrinting):
                print(numberOfPrinting - i, ": ", text)

def reversPrinter2 (numberOfPrinting: int, text: str):
    if isinstance(numberOfPrinting, int) and isinstance(text, str):
        for i in range(numberOfPrinting, 0, -1):
                print(i ,": ", text)

reversPrinter2(6,"In the name of Allah")
reversPrinter(99, "ya ali")
triangle("S",7)
rectangle("S",5,6)


