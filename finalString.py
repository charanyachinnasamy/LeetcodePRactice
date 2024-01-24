def finalString(s):
    result = ''
    for i in range(0,len(s)):
        if s[i] == 'i':
            result = result[::-1]
        else:
            result = result + s[i]

    return result

print(finalString("poiinter"))
