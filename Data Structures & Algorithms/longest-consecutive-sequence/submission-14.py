class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        maxcount = 1
        count = 1
        if nums == []: return 0
        for i in range(1,len(nums)):
            if (abs(nums[i] - nums[i-1]) == 1):
                count += 1
                print(count)
                if count > maxcount:
                    maxcount = count
            else:
                count = 1
        return(maxcount)