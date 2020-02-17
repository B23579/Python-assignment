def ClockX(minute): 
    """ This function takes as input the number of minute
    and returns a string that format teh number into hours:minute"""
    minute=int(minute)
    
    hours = minute//60
    minute = minute - hours*60
    if hours <10 : 
        hours='0'+ str(hours)
    else :
        hours=str(hours)
    if minute<10 : 
        minute = str(minute) + '0'
    else:
        minute = str(minute)
        
    print("the time is",hours + ':' + minute)

minute = input("Enter the number of your minute ")
ClockX(minute)