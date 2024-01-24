def maximumNumberOfStringPairs(words):
    i =0
    rever=""
    c = 0
    while (i<len(words)):

        for j in range(len(words[i])-1,-1,-1):
            rever = words[i][1]+words[i][0]

        if rever in words and rever != words[i]:
            c = c + 1
            words.remove(rever)
        rever = ""
        i = i + 1
    return c

print(maximumNumberOfStringPairs(["ab","ba","cc"]))



