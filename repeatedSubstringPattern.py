def repeatedSubstringPattern(s):
    l = len(s)
    first_chara = s[0]
    repeated_string = ""
    index = 0
    for i in range(0,l):
        if s[i] != first_chara and i !=0:
            repeated_string = repeated_string + s[i]
        elif i ==0:
            repeated_string = s[0]
        elif s[i] == first_chara:
            index = i
            break
        else:
            continue
    length = len(repeated_string)
    i = index
    if (l%length) != 0:
        return False
    while(i+length<=l):
        string_check = s[i:i+length]
        if repeated_string != string_check:
            return False
        i = i + length
    return True



print(repeatedSubstringPattern("abaababaab"))




