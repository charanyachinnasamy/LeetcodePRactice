def twoSum(nums,target):
    for i in range(0,len(nums)):
        if target-nums[i] in nums and nums.index(target-nums[i])!=i:
            new_index = nums.index(target-nums[i])
            if nums[i]+nums[new_index]== target:
                return [i,new_index]
        elif nums[i] - target in nums and nums.index(nums[i]-target) != i:
            new_index = nums.index(nums[i]-target)
            if nums[i] + nums[new_index] == target:


                return [i,new_index]
        else:
            continue
    return None

print(twoSum([2,1,9,4,4,56,90,3],8))
