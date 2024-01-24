def checkIfPangram(sentence):
    if len(sentence)<26:
        print("less length")
        return False
    alphabet={}
    for i in range(0,len(sentence)):
        if sentence[i] not in alphabet:
            alphabet[sentence[i]]=1
        else:
            alphabet[sentence[i]]+=1

    if len(alphabet)==26:
        return True
    return False

print(checkIfPangram("uwqohxamknblecdtzpisgvyfjr"))

