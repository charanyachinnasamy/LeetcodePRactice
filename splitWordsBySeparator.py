def splitWordsBySeparator(words, separator):
        """
        :type words: List[str]
        :type separator: str
        :rtype: List[str]
        """
        result=[]

        for item in words:
            for i in item.split(separator):
                if i:
                    result.append(i)




        return result
print(splitWordsBySeparator(["one.two.three","four.five","six"],"."))
