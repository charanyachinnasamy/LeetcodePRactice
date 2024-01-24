def truncateSentence(s,k):
    result = [word for word in s.split()]
    output = ""
    for i in range(k):
        output = output + " " +result[i]
    return output

print(truncateSentence("chopper is not a tanuki",5))


