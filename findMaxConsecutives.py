def findMaxConsecutiveOnes(nums):
    i = 0
    c = 0
    max_c = 0
    while(i<len(nums)):

        if nums[i] == 1:
            c = c +1
        else:
            max_c = max(max_c,c)
            c = 0

        i = i + 1
    max_c = max(max_c,c)
    return max_c

print(findMaxConsecutiveOnes([1,1,0,1,1,1]))


