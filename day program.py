# To determine the day at that the Entered date
def date(dd,mm,yyyy):
    m=[31,28,31,30,31,30,31,31,30,31,30,31]  #assinment, number of days in month's
    if(yyyy%4==0):                           #increment of 1 for a leap year in the month of feb
        m[1]=29
    days=0
    for i in range(0,mm-1,1):                #calculating the number of days in till mm months
        days+=m[i]
    if yyyy>=2000:                           #as the reference is year 2000, if year entered by user is grearter or equal to year 2000                       
        days=days+dd-1
    elif yyyy%4==0 and yyyy<2000:            #year less then 2000 and is leap year
        days=366-(days+dd)
    elif yyyy%4!=0 and yyyy<2000:            #year less then 2000 
        days=365-(days+dd)
        
    year=yyyy-2000                           #difference between year 2000 and the year provided to function
    if year>=0:
        leap=year//4                         #leap year between the years
    else:
        leap=year//4+1                       #The negetive integer tends to shift left side, so to counter that one is added to the division
        

    if year%4!=0 and yyyy>2000:              # counter the no. of leap year between non 
        leap+=1
    

    year=abs(year+leap)+days
    daynum=year%7


    if(yyyy<2000 and daynum!=0):
        k=5
        for i in range(1,daynum,1):
            k-=2
        daynum+=k
    

    if daynum==0:
        print("the day is saturday")
    elif daynum==1:
        print("the day is sunday")
    elif daynum==2:
        print("the day is monday")
    elif daynum==3:
        print("the day is tuesday")
    elif daynum==4:
        print("the day is wednesday")
    elif daynum==5:
        print("the day is thursday")
    elif daynum==6:
        print("the day is friday")
    else:
        print("does not exist")


    
    
