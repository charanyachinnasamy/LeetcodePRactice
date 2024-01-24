def sortSentence(s):
    result=[None]*len(s.split())

    for word in s.split():

        result[int(word[-1])-1]=word[:-1]
    return " ".join(result)
print(sortSentence("lGaWqAkfVIFhqBzRs3 l2 bwKhelcNiyNBpjGUN1"))
