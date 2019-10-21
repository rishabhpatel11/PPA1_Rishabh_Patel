import math

def distance(x1, y1, x2, y2):
    x1m, y1m, x2m, y2m = (1,1,1,1)
    try:
        if(x1.startswith("-")):
            x1=x1[1:]
            x1m=-1
        x1=x1m*float(x1)
    except TypeError:
        print("Expected number for x1")
    try:
        if(y1.startswith("-")):
            y1=y1[1:]
            y1m=-1
        y1=y1m*float(y1)
    except TypeError:
        print("Expected number for y1")
    try:
        if(x2.startswith("-")):
            x2=x2[1:]
            x2m=-1
        x2=x2m*float(x2)
    except TypeError:
        print("Expected number for x2")
    try:
        if(y2.startswith("-")):
            y2=y2[1:]
            y2m=-1
        y2=y2m*float(y2)
    except TypeError:
        print("Expected number for y2")
        
    dist=math.sqrt(((x2-x1)*(x2-x1)) + ((y2-y1)*(y2-y1)))
    return [x1,y1,x2,y2,"%.5f" % round(dist,5)]

