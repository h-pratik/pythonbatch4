import math
def root(a,b,c):
    d= (b*b)-(4*a*c)
    global r1,r2, realpart,imapart
    print(d)
    if(d>0):
        r1 = (-b+math.sqrt(d))/(2*a)
        r2 = (-b-math.sqrt(d))/(2*a)
        return 1
    elif(d==0):
        r1 = r2 = (-b)/(2*a)
        print(r2)
        return 2
    else:
        realpart = -b/(2*a)
        imapart = (math.sqrt(-d))/(2*a)
        return 3

print("Enter the Coefficient A: ")
a = float(input())
print("Enter the coefficient B: ")
b= float(input())
print("Enter the coefficient C: ")
c = float(input())
r1 = 0
r2 = 0
realpart = 0
imapart = 0
t = root(a,b,c)
if( t == 1):
    print("Roots are Real and Distinct")
    print("Roots are ",r1,r2)
elif( t==2):
    print("Roots are Real and equal")
    print("Roots are ",r1, r2)
elif (t==3):
    print("Roots are Not Real")
    print("Roots are Root 1 = ",realpart,"+",imapart,"i and Root 2 = ",realpart,"-",imapart,"i")