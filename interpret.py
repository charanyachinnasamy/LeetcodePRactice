def interpret(command):
    i = 0
    result =""
    while(i<len(command)):
        if command[i] == 'G':
            result = result + 'G'
            i = i + 1
        elif command[i] == '(':
            i = i + 1
        elif command[i] == 'a':
            i = i + 3
            result = result + 'al'
        else:
            result = result + 'o'
            i = i + 1
    return result

print(interpret("(al)G(al)()()G"))



