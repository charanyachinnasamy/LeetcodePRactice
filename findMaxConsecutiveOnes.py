def findMaxConsecutiveOnes(nums):
    c = 0
    max_c = 0
    for num in nums:
        if num == 1:
            c = c + 1
        else:
            max_c = max(max_c,c)
            c = 0
    return max(max_c,c)

print(findMaxConsecutiveOnes([1,0,1,1,0,1]))



