def addToArrayForm(num, k):
        """
        :type num: List[int]
        :type k: int
        :rtype: List[int]
        """
        actual_num=""
        result=0
        actual_result=[]
        for item in num:
            actual_num = actual_num + str(item)
        result = int(actual_num)+k
        actual_result =[int(x) for x in str(result)]
        return actual_result
print(addToArrayForm([2,1,5],806))
