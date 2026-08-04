class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mydict = {};
        for i in range(len(nums)):
            if nums[i] in mydict:
                return True;
            mydict[nums[i]] = i;  
        return False;