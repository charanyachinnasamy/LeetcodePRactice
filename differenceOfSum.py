def differenceOfSum(nums):
    actual_sum = 0
    digit_sum = 0
    for num in nums:
        actual_sum = actual_sum + num
        n = str(num)
        i = 0
        while(i<len(n)):
            digit_sum= digit_sum+int(n[i])
            i = i + 1
    return abs(actual_sum-digit_sum)

print(differenceOfSum([1,2,3,4]))
