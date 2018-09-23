time = input('Please enter your goal marathon time (x:xx:xx): ')

def total_time():
    separated_time = str(time).split(':')

    hours = int(separated_time[0])
    minutes = int(separated_time[1])
    try:
        seconds = int(separated_time[2])
    except:
        seconds = 0

    print('\nYour total time is ' + str(hours)   + ' hours, '
                                  + str(minutes) + ' minutes, '
                                  + str(seconds) + ' seconds')

    return (hours * 60 * 60) + (minutes * 60) + seconds

def seconds_to_minutes_and_hours(seconds):
    hours = seconds // 3600
    remaining_seconds = seconds % 3600
    minutes = remaining_seconds // 60
    remaining_seconds = seconds % 60
    seconds = remaining_seconds % 60

    if hours > 0:
        formatted_hours = str(int(hours)) + ":"
    else:
        formatted_hours = ''

    formatted_minutes = str(int(minutes)).zfill(2) + ":"
    formatted_seconds = str(int(seconds)).zfill(2)
    return formatted_hours + formatted_minutes + formatted_seconds

def marathon_mile_splits():
    splits = list(range(1, 27))
    splits.append(13.1)
    splits.append(26.2)
    splits.sort()
    return splits

total_seconds = total_time()

for x in marathon_mile_splits():
    seconds_per_mile = total_seconds / 26.2
    print(str(x) + " -- " + str(seconds_to_minutes_and_hours(seconds_per_mile * x)))
