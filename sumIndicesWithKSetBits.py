def sumIndicesWithKSetBits(nums,k):
    s = 0
    for i in range(0,len(nums)):
        b = ""
        index=i
        while(i>0):


            b = str(i%2)+ b
            i = i // 2


        c= b.count('1')
        if c == k:

            s = s + nums[index]
    return s




print(sumIndicesWithKSetBits([5,10,1,5,2],1))


