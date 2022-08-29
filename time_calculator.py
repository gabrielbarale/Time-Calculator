def add_time(start, duration, current_day = ""):

    days = 0
    weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

    #Separating the given times into minutes, hours and period
    start_hour = start.split(":")[0]
    start_minute = start.split(":")[1].split()[0]
    start_period = start.split(":")[1].split()[1]
    duration_hour = duration.split(":")[0]
    duration_minutes = duration.split(":")[1]

    #Calculation of the new hours and minutes
    new_hour = int(duration_hour) + int(start_hour)
    new_minute = int(duration_minutes) + int(start_minute)
    new_period = start_period

    #Changing extra minutes to hours
    while new_minute >= 60:
        new_minute -=60
        new_hour +=1

    #Changing extra hours to days
    while new_hour >= 12:
        new_hour -= 12
        if new_period == "PM":
            new_period = "AM"
            days += 1
        else: 
            if new_period == "AM":
                new_period = "PM"
              
    #Changing to the requested format
    if new_hour == 0:
        new_hour = 12

    if new_minute < 10:
        new_time = str(new_hour) + ":" + "0" + str(new_minute) + " " + new_period
    else:
        new_time = str(new_hour) + ":" + str(new_minute) + " " + new_period
    
    if current_day != "":
        aux = weekdays.index(current_day.capitalize())
        new_day = weekdays[(days + aux) % 7]
        new_time += ", " + new_day

    if days == 1:
        new_time += " (next day)"
    else:
        if days > 1:
            new_time += " (" + str(days) + " days later)"
        
    return new_time