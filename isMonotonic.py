def isMonotonic(nums):

        if len(nums)<2:
            return True

        c = 0
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:

                if c == 0:
                    c = 1

                elif c == 2:
                    return False

            elif nums[i]> nums[i -1] :
                if c == 0:
                    c =  2

                elif c == 1:
                    return False





        return True

print(isMonotonic([1,1,0]))

