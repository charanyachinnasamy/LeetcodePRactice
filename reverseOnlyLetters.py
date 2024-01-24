
def reverseOnlyLetters(s):
    l = len(s)
    result = ""
    char=[]

    for i in range(0,l):
        if s[i].isalpha():
            char.append(s[i])


    for i in range(0,l):
        if s[i].isalpha():
            result=result+char[-1]
            char.pop(-1)
        else:
            result = result + s[i]




    return result

print(reverseOnlyLetters("Test1ng-Leet=code-Q!"))
