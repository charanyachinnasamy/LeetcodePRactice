def createTargetArray(nums,index):
    target_array=[]
    i = 0
    for i in range(0,len(nums)):

        target_array.insert(index[i],nums[i])
    return target_array

print(createTargetArray([1],[0]))
