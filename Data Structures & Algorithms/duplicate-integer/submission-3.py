class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mydict = {}
        for n in range(len(nums)):
            if (nums[n] in mydict):
                return True
            else:
                mydict[nums[n]] = n
        return False
        
        