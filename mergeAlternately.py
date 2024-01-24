def mergeAlternately(word1,word2):
    i = 0
    j = 0
    result = " "
    len_word1 = len(word1)
    len_word2 = len(word2)
    while (i<len(word1)and j<len(word2)):
        result = result + word1[i] + word2[j]
        i = i + 1
        j = j + 1
    if (i!=len_word1):
        result = result + word1[i:]
    if (j!=len_word2):
        result= result +  word2[j:]
    return result

print(mergeAlternately("abcd","pq"))
