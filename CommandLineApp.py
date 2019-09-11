import RetirementCalculator
import SplitTipCalculator
import BMICalculator
import DistanceCalculator

def function():
    print('Enter a number to select a function from the list:')
    print('1. Body Mass Index Calculator')
    print('2. Retirement Age Calculator')
    print('3. Shortest Distance Calculator')
    print('4. Split the Tip')
    choice=(int)(input("-->"))
    if(choice == 1):
        feet=input("Enter the feet part of your total height as a whole number: \n")
        inches=input("Enter the inches part of your total height as a whole number: \n")
        weight=input("Enter your weight in pounds as a number: \n")
        output=BMICalculator.bmi(feet,inches,weight)
        print("Your Body Mass Index is: " + str(output[0]))
        print("Your Body Mass Index falls under the category: " + output[1])
        
    if(choice == 2):
        age=input("Enter your age as a whole number: \n")
        salary=input("Enter your annual salary as a number: \n")
        saved=input("Enter the percent of your salary you plan on saving yearly as a number: \n")
        goal=input("Enter your desired retirement savings goal as a number: \n")
        output=RetirementCalculator.retirement(age,salary,saved,goal)
        if(output[1] == -1):
            print(output[0])
        else:
            print(output[0] + str(output[1]))

    if(choice == 3):
        print("Refer to the 2 points as: (x1,y1) and (x2,y2)")
        x1=input("Enter x1: \n")
        y1=input("Enter y1: \n")
        x2=input("Enter x2: \n")
        y2=input("Enter y2: \n")
        print("The shortest distance between the points is: " + str(DistanceCalculator.distance(x1,y1,x2,y2)))

    if(choice == 4):
        print("Calculator adds a 15% tip rounded to the nearest cent")
        total=input("Enter the total of the bill as a number without any $ signs: \n")
        guests=input("Enter the number of guests you want to split the bill for: \n")
        output=SplitTipCalculator.splitTip(total,guests)
        print("Total with tip: " + str(output[len(output)-1]))
        for i in range(len(output)-1):
            print("guest"+str(i)+"-"+str(output[i]))
    print("\n\nEnter 1 to exit now or 0 to return to the menu")
    global exit
    exit=(int)(input("-->"))
    if(exit != 1 and exit !=0):
        print("Invalid choice, exiting application...")
    if(exit ==0 ):
        print("\n\n\n")

exit=0
while(exit==0):
    function()