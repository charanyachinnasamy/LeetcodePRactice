def findWordsContaining(words,x):
        result = []
        for i in range(0,len(words)):
            if x in words[i]:
                result.append(i)
        return result

print(findWordsContaining(["abc","bcd","aaaa","cbc"],'a'))
