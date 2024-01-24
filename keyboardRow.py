


def findWords(words):
    l1=['q','w','e','r','t','y','u','i','o','p']
    l2=['a','s','d','f','g','h','j','k','l']
    l3=['z','x','c','v','b','n','m']
    flag = 0
    result = []
    wordold=""
    for word in words:
        if len(word) == 1:
                result.append(word)
                continue
        wordold=word
        word= word.lower()
        if word[0] in l1:
            flag = 0
        elif word[0] in l2:
            flag = 1
        else:
            flag = 2
        print(word,flag)
        for i in range(1,len(word)):
            print(word[i])
            if word[i] in l1 and flag == 0:
                continue
            elif word[i] in l2 and flag == 1:
                continue
            elif word[i] in l3 and flag == 2:
                continue
            else:
                flag = -1
                break
        print(i)
        if i == len(word)-1 and flag !=-1:
            result.append(wordold)



    return result





print(findWords(["abdfs","cccd","a","qwwewm"]))

