import os
import re
from pathlib import Path
class BaseTools: 
    @staticmethod
    def StringListToInt(numbers: list)-> list:
        intedList = list()
        for i in numbers:
            intedList.append(int(i))
        return intedList
    
    @staticmethod
    def AddToFile(path: str, fileName: str, context: str) -> str:
            fullPath = os.path.join(path, fileName)
            newFullPath = ""
            #اگر در هنگام اضافه کردن عدد به فایل فایلی به وجود بیاد که قبلا توی دایرکتوری بوده باشه در اینصورت لوپ رو از اول بر میگردونیم و یک عدد بیشتر جایگزینش می کنیم تا مطمئن بشیم که فایل ما حتما جدیده
            whileCount = 1
            while True:     
                #اگر پوشه داده شده نبود
                if os.path.exists(path):
                    #اگر فایل داده شده بود یا نبود 
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
                                file.close()
                            return newFullPath
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
                                file.close()
                            return newFullPath
                    # اگر فایلی نبود
                    else:
                        with open(fullPath, 'a') as file:
                            file.write(context)
                            file.close()
                        return fullPath
                else:
                    #پوشه اگر موجو نباشه باید بسازیمش 
                    os.makedirs(path)
                    print("directory wasn't exist, we create a new one :-) ")
    
    # if the Save_Log_Path.txt weren't exist. then we create a new one with our defult value
    def CreateFile(folderPath = os.getcwd(), fileName = "Save_Log_Path.txt") -> bool:
        if os.path.isdir("mylogs") == False:  
            os.mkdir("myLogs")
        filePath = os.path.join(folderPath, "myLogs", fileName)
        if os.path.isfile(filePath):
            return filePath
        else:
            logSavePath = os.path.join(folderPath, "myLogs")
            with open(filePath, 'x') as file:
                file.write(BaseTools.CustomeLog(Log_type= 2, save_Log_Path= logSavePath))
                file.close()
            return filePath
        
    @staticmethod
    def CustomeLog(oprationNumber: str = "0", functionName: str ="", userInput: str = "None", userOutPut: str = "None", errorText: str = "",
                   Log_type: int = 0, save_Log_Path: str = "") -> str:
        if isinstance(functionName, str):
            match Log_type:
                #prosses log
                case 1:
                    if oprationNumber == 1:
                        return str(("Author: Mohammad Sajjad Sharifi Panah"+"\nOpration Name: "+ str(oprationNumber) + "\nThe Function That Used: " +  functionName + "\ninput: " + str(userInput) +
                                    "\nout_put: "+ str(userOutPut) + "\n--------------------------------------------------"))
                    #else   
                    return str(("\nOpration Name: "+ str(oprationNumber) + "\nThe Function That Used: " +  functionName + "\ninput: " + str(userInput) +
                                "\nout_put: "+ str(userOutPut) + "\n--------------------------------------------------"))
                #create a Save_Log_Path Log
                case 2:
                    return str("Save Log Path =" + save_Log_Path + "\nFile Name = LogText.txt")
                # error log
                case 3 :
                    if errorText != "":
                        return str(("\nAuthor: Mohammad Sajjad Sharifi Panah"+"\nSorry Something Went Wrong :-("+"\nOpration Name: "+ str(oprationNumber) + "\nLast Function That Used: " +  functionName + "\ninput: " + str(userInput) +
                                    "\nout_put: Error" +"\nError Massage: "+ errorText + "\n--------------------------------------------------"))
                case _:
                    return ""
            
    @staticmethod
    #ما یک فایلی داریم که مشخصات محل ذخیره لاگ هامون رو توش میزاریم. برای اینکه بخواهیم بخونیمش از این تابع استفاده میکنیم
    def ExtractSaveLogPathAndNameFromFile(filePath: str)-> list:
        fileList =""
        with open(filePath, 'r')as file:
            fileList = file.readlines()
            file.close()
        
        return fileList
    
    @staticmethod
    def CurrentAppLocation() -> str:
        #پیدا کردن مسیر اجرا شدن فعلی برنامه
        return os.getcwd()
    
    @staticmethod
    def isFileExist(path: str) -> bool:
        return os.path.isfile(path)
        