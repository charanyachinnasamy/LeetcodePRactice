def commonChars(words):

        occur={}
        result=[]

        i = 0
        while(i<len(words[0])):

            if words[0][i] in occur:
                occur[words[0][i]] =  occur[words[0][i]] + 1
            else:
                 occur[words[0][i]] = 1

            i = i + 1



        for keys in occur:
            for i in range(1,len(words)):

                if keys in words[i]:
                    occur[keys]=min(occur[keys],words[i].count(keys))
                else:
                    occur[keys]=0
                    break
        for keys,values in occur.items():
            print(values,[keys])
            result += values * [keys]




        return result




print(commonChars(["bella","label","roller"]))
