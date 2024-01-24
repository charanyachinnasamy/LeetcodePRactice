def freqAlphabets(s):
        i = 0
        n =''
        alpha =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        result =""
        while(i+2<len(s)):
            if s[i+2] == '#':
                n=s[i]+s[i+1]
                result=result+alpha[int(n)-1]
                print(n,result,alpha[int(n)-1])
                i = i + 3
            else:
                result=result+alpha[int(s[i])-1]
                i = i + 1
        if i != len(s):
            while(i<len(s)):
                print(i)
                result=result+alpha[int(s[i])-1]
                i = i + 1

        return result

print(freqAlphabets("1326#"))
