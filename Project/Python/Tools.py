class Tools: 
    @staticmethod
    def StringListToInt(numbers: list):
        intedList = list()
        for i in numbers:
            intedList.append(int(i))
        return intedList