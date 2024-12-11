from Oprations.The_Functions import MyOprations
from Tools.Base_Tools import BaseTools
from Tools.Sub_Tools import SubTools
from colorama import init, Fore, Back, Style

#  تعداد دفعات اجرای برنامه با یک بار باز کردن
oprationCount = 0
#برای اینکه بدونیم کدوم تابع اجرا شده 
functionCheck = ""
myInput = ""
myOutPut = ""
try:
    #first we check if save_log_path.txt exists or not. if it was exist then we read it and set the location which wrote in the file to logs_path 
    #if it wasn't exist then we create our own then do the rest.
    logs_path = (BaseTools.CurrentAppLocation() + r"\Save_Log_Path.txt")
    if BaseTools.isFileExist(logs_path) == False:
       logs_path = BaseTools.CreateFile()
       logs_path = BaseTools.ExtractSaveLogPathAndNameFromFile(logs_path)
    else:
     logs_path = BaseTools.ExtractSaveLogPathAndNameFromFile(logs_path)

    print(logs_path)
    print("Wellcome to our program :-)")
    #برای اینکه برنامه ادامه پیدا کنه یا بره بیرون
    running = True
    
    # برای اینکه بفهمیم کدوم عملیات انتخاب شده
    oprationCheck = 0
    
    # اگر مساحت مثلث انتخاب شد نوعش هم بتونه انتخاب کنه
    triangleOprationCheck = 0
    
    # مقادیری که در هر عملیات از کاربر میگیریم رو به این متغیر میدیم
    values = list()

    # تا زمانی که رانینگ درست باشه برنامه اجرا میشه
    while running:
        # میخواهیم تعداد باری که کاربر از برنامه در یک بار باز کردن استفاده میکند را داشته باشیم
        # برای این اول بهش مقدار میدم چون میخوام اگر خطایی داشتم بدونم در کدوم بار این خطا رخ داده
        oprationCount += 1
        # شماره هر عملیات رو مینویسم تا یه وقت اشتباه نشه
        print(Fore.LIGHTBLUE_EX,"Oprations Number:", '\n', "1. Area Of Triangle", '\n', "2. Area Of Rectangle", '\n', "3. Proof Of Golden Ratio", '\n',
              "4. Word Reverser", Style.RESET_ALL)
        oprationCheck = input("Pls Enter Your Opration Number: ")
        
        myInput = oprationCheck
        try:
            match int(oprationCheck):
                # بر اساس شماره ایی که میگیریم تصمیم میگیریم کدوم عملیات اجرا بشه
                case 1:
                    print(Fore.LIGHTBLUE_EX,"we have 3 way to find a triangle area. which one do you want?")
                    print("Opration's Number: ",'\n', "1.Triangle Area With ThreeSide", '\n',
                        "2.Triangle Area With Two Side that next to each other And Angle", '\n',
                        "3.Triangle Area Using Height And Base", Style.RESET_ALL)
                    
                    triangleOprationCheck = input("Pls Enter Your Opration Number: ")
                    myInput = triangleOprationCheck
                    match int(triangleOprationCheck):
                        case 1:
                            functionCheck = "1.Triangle Area With ThreeSide"
                            values = input("Pls Enter Your Sides in One Line: ").split()
                            myInput = values
                            #تبدیل لیست رشتمون به عدد
                            values = BaseTools.StringListToInt(values)
                            myOutPut = MyOprations.TriangleAreaWithThreeSide(values[0], values[1], values[2])
                            print("Your Answer is: ", Fore.YELLOW, myOutPut , Style.RESET_ALL)
                        case 2:
                            functionCheck = "2.Triangle Area With Two Side that next to each other And Angle"
                            # مقادیر رو به صورت لیست در میاریم تا نخواهیم متغیر های الکی درست کنیم
                            values = input("Pls Enter Your Sides and angle in One Line, note that enter the angle at last!: ").split()
                            myInput = values
                            values = BaseTools.StringListToInt(values)
                            myOutPut = MyOprations.TriangleAreaWithTwoSideAndAngle(values[0], values[1], values[2])
                            print("Your Answer is: ", Fore.YELLOW, myOutPut, Style.RESET_ALL)
                        
                        case 3:
                            functionCheck = "3.Triangle Area Using Height And Base"
                            values = input("Pls Enter Your Height first then Base in One Line: ").split()
                            myInput = values
                            values = BaseTools.StringListToInt(values)
                            myOutPut = MyOprations.TriangleAreaUsingHeightAndBase(values[0], values[1])
                            print("Your Answer is: ", Fore.YELLOW, myOutPut, Style.RESET_ALL)
                case 2:
                    functionCheck = "2. Area Of Rectangle"
                    values = input("Please enter the length and width in order: ").split()
                    myInput = values
                    values = BaseTools.StringListToInt(values)
                    myOutPut =  MyOprations.RectangleArea(values[0], values[1])
                    print("Your Answer is: ", Fore.YELLOW, myOutPut, Style.RESET_ALL)
                case 3:
                    functionCheck = "3. Proof Of Golden Ratio"
                    # با وجود اینکه گفتیم متغیر ولیو لیست هست اما در پایتون هرچی بدی به همون جنس تغییر میکنه برای همین نیازی نیست که به صورت لیست مقدار بگیریم
                    print("This Opration is a proof of golden ratio, anything you put the answer will be always 1. becouse (sinx)^2 + (cosx)^2 = 1")
                    values = input("Please enter your value for x: ")
                    myInput = values
                    myOutPut = MyOprations.ProofOfGoldenRatio(int(values))
                    print("Your Answer is: ", Fore.YELLOW, myOutPut, Style.RESET_ALL)
                case 4:
                    functionCheck = "4. Word Reverser"
                    values = input("Pls Enter Your Word or Text in One Line: ")
                    myInput = values
                    myOutPut = MyOprations.WordReverser(values)
                    print("Your Answer is: ", Fore.YELLOW, myOutPut, Style.RESET_ALL)
        except:
            break
        else:
            if oprationCount ==1:
                logs_path = BaseTools.AddToFile(path= logs_path[0].split("=")[1].strip(), fileName= logs_path[1].split("=")[1].strip(),
                                                context= BaseTools.CustomeLog(oprationNumber= oprationCount, functionName= functionCheck,Log_type= 1,
                                                                              userInput= myInput, userOutPut= myOutPut))
            else:
                # وقتی فایل ساخته بشه دیگه لازم نیست دوباره ساخته بشه. بلکه کافیه بهش یه چیزی اضافه بشه
                SubTools.AddToFile(path= logs_path, context= BaseTools.CustomeLog(Log_type= 1,oprationNumber= oprationCount, functionName= functionCheck,
                                                                                  userInput= myInput))
            #حالا کاربر تصمیم میگیره که ادامه بده یا برنامه رو ببنده هر جا این کد بود یعنی این کار داره صورت میگیره
            running = MyOprations.WantToDoItAllAgain()
    
    raise ValueError                
                
except Exception as exception:
    #اگر خطایی خوردیم برامون چاپ میکنه
    print(Fore.RED, exception.__class__.__name__, '\n', exception, Style.RESET_ALL)
    if oprationCount ==1:
        BaseTools.AddToFile(path= logs_path[0].split("=")[1].strip(), fileName= logs_path[1].split("=")[1].strip(),
                            context= BaseTools.CustomeLog(oprationNumber= oprationCount, functionName= functionCheck,
                                                          errorText= exception.__class__.__name__, Log_type= 3))
    else:
        # وقتی فایل ساخته بشه دیگه لازم نیست دوباره ساخته بشه. بلکه کافیه بهش یه چیزی اضافه بشه
        SubTools.AddToFile(path= logs_path, context= BaseTools.CustomeLog(oprationNumber= oprationCount, functionName= functionCheck, Log_type= 3,
                                                                          userInput= myInput,errorText= exception.__class__.__name__))

finally:
    # چه به خطا بخوریم چه نخوریم باید در نهایت خودمون بتونیم برنامه رو ببندیم
    input("Press any key to continue")

