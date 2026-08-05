class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}
        for num in range(len(nums)):
            if ((target - nums[num]) in mydict):
                return([mydict[target-nums[num]], num])
            mydict[nums[num]] = num