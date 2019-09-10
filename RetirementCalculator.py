import math
def retirement(age, salary, saved, goal):
    try:
        age=(int)(age)
    except TypeError:
        print("Expected a whole number for age")
    
    if( (age > 99) or (age < 1) ):
        raise Exception("Invalid range for age")

    try:
        salary=(float)(salary)
    except TypeError:
        print("Expected number for salary")

    try:
        saved=(float)(saved)
    except TypeError:
        print("Expected number for saved")

    try:
        goal=(float)(goal)
    except TypeError:
        print("Expected number for goal")

    percent=saved/100.0
    yearlySaved=(salary*percent) + (.35*(salary*percent))
    yearsRequired=math.ceil(goal/yearlySaved)
    if(age+yearsRequired >= 100):
        return ["Savings goal will not be met in the current lifespan", -1]
    return ["Savings goal will be met at age: ", (age+yearsRequired)]
