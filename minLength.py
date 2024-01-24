def minLength(s):
    while (s.find('AB') != -1 or s.find('CD')!= -1):
        s= s.replace('AB','')
        s =s.replace('CD','')

    return len(s)

print(minLength("ACBBD"))
