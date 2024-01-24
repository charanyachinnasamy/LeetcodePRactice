def mostWordsFound(sentences):
    c = 0
    for sentence in sentences:
         t = len(sentence.split())
         if t>c:
             c = t
    return c

print(mostWordsFound(["please wait", "continue to fight", "continue to win"]))

