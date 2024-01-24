def isLongPressedName(name,typed):
    i = 0
    j = 0
    while(j <len(typed)):
        if i<len(name) and name[i] ==  typed[j]:
            i = i + 1
        elif j == 0 or typed[j] != typed[j-1]:
            return False
        j = j + 1


    return i == len(name)


print(isLongPressedName("alex","aaleexa"))




