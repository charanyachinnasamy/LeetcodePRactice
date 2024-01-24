def canBeTypedWords(text,brokenletters):
    letters = []
    c = 0
    flag = 0
    for char in brokenletters:
        letters.append(char)
    for word in text.split():
        print(word)

        for char in word:
            print(char)
            if char in brokenletters:
                flag = -1
                break
        if flag != -1:
            c = c +1
        else:
            flag = 0




    return c

print(canBeTypedWords("leet","e"))


