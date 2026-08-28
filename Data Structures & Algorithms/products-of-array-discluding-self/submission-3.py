# 1 2 3 4 nums
# 1 1 2 6 prev
# 24 12 4 1 suf
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [0] * len(nums)
        suf = [0] * len(nums)
        result = [0] * len(nums)
        pref[0] = 1
        suf[len(nums)-1] = 1
        for i in range(1, len(nums), 1):
            pref[i] = nums[i-1] * pref[i-1]
        for i in range(len(nums)-2, -1, -1):
            suf[i] = suf[i+1] * nums[i+1]
        for i in range(len(nums)):
            result[i] = pref[i] * suf[i]
        return(result)
