def digitCount(num):
    i = 0
    while(i<len(num)):
        if num.count(str(i)) != int(num[i]):
            return False
        i = i + 1
    return True

print(digitCount("1210"))
