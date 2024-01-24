def twoOutOfThree(nums1,nums2,nums3):
        result = {}
        endresult=[]
        for num in nums1:
            if num in result:
                result[num].add(1)
            else:
                result[num]={1}
        for num in nums2:
            if num in result:
                result[num].add(2)
            else:
                result[num]={2}
        for num in nums3:
            if num in result:
                result[num].add(3)
            else:
                result[num]={3}
        for key,value in result.items():
            if len(value)>=2:
                endresult.append(key)
        return endresult

print(twoOutOfThree([1,2,2],[4,3,3],[5]))

