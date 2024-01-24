def dominantIndex(nums):
        a = sorted(nums)
        if a[-2]*2 <= a[-1]:
          return nums.index(a[-1])
        return -1



print(dominantIndex([1,2,3,4]))
