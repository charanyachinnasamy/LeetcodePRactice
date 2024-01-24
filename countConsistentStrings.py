def countConsistentStrings(allowed,words):
    result = 0
    for word in words:
        i = 0
        while (i<len(word)):
            if word[i] in allowed:
                i = i + 1
            else:
                break
        if i == len(word):
            result = result+1
    return result

print(countConsistentStrings("abc",["a","b","c","ab","ac","bc","abc"]))


