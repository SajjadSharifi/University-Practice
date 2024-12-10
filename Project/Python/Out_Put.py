from The_Functions import MyOprations
from Tools import Tools
from colorama import init, Fore, Back, Style
try:
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
        # شماره هر عملیات رو مینویسم تا یه وقت اشتباه نشه
        print(Fore.LIGHTBLUE_EX,"Oprations Number:", '\n', "1. Area Of Triangle", '\n', "2. Area Of Rectangle", '\n', "3. Proof Of Golden Ratio", '\n',
              "4. Word Reverser", Style.RESET_ALL)
        oprationCheck = int(input("Pls Enter Your Opration Number: "))
        match oprationCheck:
            # بر اساس شماره ایی که میگیریم تصمیم میگیریم کدوم عملیات اجرا بشه
            case 1:
                print(Fore.LIGHTBLUE_EX,"we have 3 way to find a triangle area. which one do you want?")
                print("Opration's Number: ",'\n', "1.Triangle Area With ThreeSide", '\n',
                      "2.Triangle Area With Two Side that next to each other And Angle", '\n',
                      "3.Triangle Area Using Height And Base", Style.RESET_ALL)
                
                triangleOprationCheck = int(input("Pls Enter Your Opration Number: "))
                match triangleOprationCheck:
                    case 1:
                        values = input("Pls Enter Your Sides in One Line: ").split()
                        #تبدیل لیست رشتمون به عدد
                        values = Tools.StringListToInt(values)
                        print("Your Answer is: ", Fore.YELLOW, MyOprations.TriangleAreaWithThreeSide(values[0], values[1], values[2]), Style.RESET_ALL)
                        
                        #حالا کاربر تصمیم میگیره که ادامه بده یا برنامه رو ببنده هر جا این کد بود یعنی این کار داره صورت میگیره
                        running = MyOprations.WantToDoItAllAgain()
                    case 2:
                        # مقادیر رو به صورت لیست در میاریم تا نخواهیم متغیر های الکی درست کنیم
                        values = input("Pls Enter Your Sides and angle in One Line, note that enter the angle at last!: ").split()
                        values = Tools.StringListToInt(values)
                        print("Your Answer is: ", Fore.YELLOW, MyOprations.TriangleAreaWithTwoSideAndAngle(values[0], values[1], values[2]), Style.RESET_ALL)
                        running= MyOprations.WantToDoItAllAgain()
                    case 3:
                        values = input("Pls Enter Your Height first then Base in One Line: ").split()
                        values = Tools.StringListToInt(values)
                        print("Your Answer is: ", Fore.YELLOW, MyOprations.TriangleAreaUsingHeightAndBase(values[0], values[1]), Style.RESET_ALL)
                        running = MyOprations.WantToDoItAllAgain()
            case 2:
                values = input("Please enter the length and width in order: ").split()
                values = Tools.StringListToInt(values)
                print("Your Answer is: ", Fore.YELLOW, MyOprations.RectangleArea(values[0], values[1]), Style.RESET_ALL)
                running = MyOprations.WantToDoItAllAgain()
            case 3:
                # با وجود اینکه گفتیم متغیر ولیو لیست هست اما در پایتون هرچی بدی به همون جنس تغییر میکنه برای همین نیازی نیست که به صورت لیست مقدار بگیریم
                print("This Opration is a proof of golden ratio, anything you put the answer will be always 1. becouse (sinx)^2 + (cosx)^2 = 1")
                values = int(input("Please enter your value for x: "))
                print("Your Answer is: ", Fore.YELLOW, MyOprations.ProofOfGoldenRatio(values), Style.RESET_ALL)
                running = MyOprations.WantToDoItAllAgain()    
            case 4:
                values = input("Pls Enter Your Word or Text in One Line: ")
                print("Your Answer is: ", Fore.YELLOW, MyOprations.WordReverser(values), Style.RESET_ALL)
                running = MyOprations.WantToDoItAllAgain()
                
except Exception as exception:
    #اگر خطایی خوردیم برامون چاپ میکنه
    print(Fore.RED, exception.__class__.__name__, '\n', exception, Style.RESET_ALL)
    

finally:
    # چه به خطا بخوریم چه نخوریم باید در نهایت خودمون بتونیم برنامه رو ببندیم
    input("Press any key to continue")

