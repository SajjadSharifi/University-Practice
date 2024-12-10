import os
import re

class Tools: 
    @staticmethod
    def StringListToInt(numbers: list)-> list:
        intedList = list()
        for i in numbers:
            intedList.append(int(i))
        return intedList
    
    @staticmethod
    #این متد برای اضافه کردن متن به فایلی که قبلا وجود داشته یا نداشته استفاده میشه
    def Addtofile(path: str, fileName: str, context: str, addToNewFile: bool = False) -> bool:
        fullPath = os.path.join(path, fileName)
        newFullPath = ""
        #شاید نخواهیم که یه فایل جدید اضافه کنیم و بخواهیم به آخر فایلم.ن یه چیزی اضافه کنیم
        if addToNewFile == True:
            #اگر در هنگام اضافه کردن عدد به فایل فایلی به وجود بیاد که قبلا توی دایرکتوری بوده باشه در اینصورت لوپ رو از اول بر میگردونیم و یک عدد بیشتر جایگزینش می کنیم تا مطمئن بشیم که فایل ما حتما جدیده
            whileCount = 1
            while True:     
                #اگر پوشه داده شده نبود
                if os.path.exists(path): 
                    if os.path.isfile(fullPath):
                        #پیدا کردن عدد در اسم فایل
                        findNumberInFileName = re.search(r'(\d+)', fullPath)
                        
                        if findNumberInFileName:
                            lastNumber = int(findNumberInFileName.group(1))
                            newFullPath = fullPath.replace(str(lastNumber), str(lastNumber + whileCount))
                            if os.path.isfile(newFullPath):
                                whileCount += 1
                                continue
                            with open(newFullPath, 'a') as file:
                                file.write(context)
                            print("done")
                            return True
                        # اگر شماره ایی نداشت
                        else:
                            fileNameParts = fileName.split(".")
                            lastPartOfTheFileName = fileNameParts[0]
                            newFileName = fileName.replace(lastPartOfTheFileName, (lastPartOfTheFileName + f"{whileCount}"))
                            newFullPath = os.path.join(path, newFileName)
                            if os.path.isfile(newFullPath):
                                whileCount += 1
                                continue
                            with open(newFullPath, 'a') as file:
                                file.write(context)
                            print("done")
                            return True
                    # اگر فایلی نبود
                    else:
                        with open(fullPath, 'a') as file:
                            file.write(context)
                        print("done")  
                        return True
                else:
                    #پوشه اگر موجو نباشه باید بسازیمش 
                    os.makedirs(path)
                    print("directory wasn't exist, we create a new one :-) ")
        else:
            with open(fullPath, "a") as file:
                file.write(context)
            print("appending done")
            return True