print() # spacing
print("Convert between 12 and 24 hour clock system")
print("Enter the current time:")
print() # spacing
# enter current time
hours = int(input("Enter the hours (0-23): "))
minutes = int(input("Enter the minutes (0-59): "))
print() # spacing

def time_conversion_func():
    # current time, remove later, display
    if hours == 00:
        current_time = f"Current time: {hours:02d}:{minutes}" # hours:02d = 00:23 instead of 0:23
    else:
        current_time = f"Current time: {hours}:{minutes}"
    # convert the current time to minutes
    hours_in_minutes = (hours * 60) // 1 # floor division, int returned
    current_time_in_minutes = hours_in_minutes + minutes

    # 12hr in minutes
    time_in_minutes = (60 * 12) // 1

    if hours < 12: # 12hr to convert to 24hr system
        time = current_time_in_minutes + time_in_minutes
        # change the time to hours and minutes

        hour = time // 60
        minute = time % 60

        # display the time
        result_time = f"Time in 24hr system: {hour}:{minute}"
        print() # spacing
    elif hours == 12:
        time = current_time_in_minutes - time_in_minutes
        # change the time to hours and minutes

        hour = time // 60
        minute = time % 60

        # display the time
        result_time = f"Time in 24hr system: {hour:02d}:{minute}"
        print() # spacing
    else: # 24hr to convert to 12hr system
        time = current_time_in_minutes - time_in_minutes
        # change the time to hours and minutes

        hour = time // 60
        minute = time % 60

        # display the time
        result_time = f"Time in 12hr system: {hour}:{minute}"
        print() # spacing

    return print(f"{current_time}\n{result_time}")

if __name__ == "__main__":
    time_conversion_func()
