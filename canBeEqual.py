def canBeEqual(s1,s2):
    if s1 == s2:
        return True
    if s1[2]+s1[1]+s1[0]+s1[3] == s2:
        return True
    if s1[0]+s1[3]+s1[2]+s1[1] == s2:
        return True

    if s1[2]+s1[3]+s1[0]+s1[1] == s2:
        return True
    return False

print(canBeEqual("abcd","dacb"))


