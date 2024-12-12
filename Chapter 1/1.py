
"""
بسم الله الرحمن الرحیم
محمد سجاد شریفی پناه

1.  How many seconds are there in 42 minutes 42 seconds?

2.  How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.

3.  If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace in seconds per mile? 
    
4.  What is your average pace in minutes and seconds per mile?

5.  What is your average speed in miles per hour?

"""

def exercise1():
    # exercise 1 : 
    print((42 * 60) + 42, "  exercise 1", "\n" ) # هر دقیقه 60 ثانیه

def exercise2():
    # exercise 2:
    print(10 //1.61,"  exercise 2","\n")
    # خروجی مقدار مایل 

def exercise3():
    # exercise 3:
    second = (42*60) + 42 
    # از ما میخواد بگیم هر مایل رو توی چند ثانیه میره؟
    averagePace = second / (10 // 1.61)
    print(averagePace,"  exercise 3", "\n")
    
def exercise4():
    # حالا سوال بالا تبدیل میکنی به اینکه هر مایل رو توی چند دقیقه میره
    minute = (42*60) + 42 
    averagePace_perMin = (minute // 60) / (10 //1.61)
    print(averagePace_perMin,"  exercise 4", "\n")

def exercise5(): 
    # در این سوال از ما سرعت متوسط رو میخواد که میشه جاب جایی تقسیم بر زمان
    hour = ((42*60) + 42)/ 3600
    averageSpeed_perHour = (int(10 //1.61)) / hour
    print(round(averageSpeed_perHour,2),"  exercise 5", "\n")

exercise1()
exercise2()
exercise3()
exercise4()
exercise5()
