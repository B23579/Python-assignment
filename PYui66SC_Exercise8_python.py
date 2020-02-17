def Military(time):
    """This function takes the time as string in AM/PM format and convert
    it to military"""
    hours = 0
    time.strip()
    if (time[5] == 'P') and (time[6] == 'M') :
         hours = int(time[0] + time[1])
         hours = hours + 12
         if hours == 24: 
             time ='00:00'
         else : 
            hours = str(hours)
            time = hours + ':' + time[3] + time[4]
    elif (time[-2] == 'A') and (time[-1] == 'M') :
         time = time[:5]
    print("The time is",time)

time = input("Enter your time in AM / PM format: ")
Military(time)