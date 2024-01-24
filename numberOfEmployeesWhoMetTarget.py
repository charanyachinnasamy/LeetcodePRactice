def numberOfEmployeesWhoMetTarget(hours,target):
    c = 0
    for hour in hours:
        if hour >= target:
            c = c + 1
    return c

