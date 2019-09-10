import math
def splitTip(total, guests):
    
    try:
        (float)(total)
    except TypeError:
        print("Expected number for total")
    else:
        if("." in total):
            decimal=total.split('.')[1]
            if(len(decimal)>2):
                raise Exception("Expected only up to 2 decimal places for the total")
        total=(float)(total)

    try:
        guests=(int)(guests)
    except TypeError:
        print("Expected whole number for guests")

    total=round(total*1.15,2)
    result=(math.floor((total/guests)*100))/100
    remainder=(total/guests)-result
    individualPayments=[result]*guests
    #print(total)
    if(remainder>0):
        current=0
        while(round(sum(individualPayments),2) != total):
            individualPayments[current]+=.01
            current+=1
            #print(sum(individualPayments))
    individualPayments.append(total)
    for x in range(len(individualPayments)):
        individualPayments[x]="%.2f" % round(individualPayments[x], 2)
    return individualPayments