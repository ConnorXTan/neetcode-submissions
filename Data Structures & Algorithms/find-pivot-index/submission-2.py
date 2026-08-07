class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ls = 0
        rs = 0

        for i in range(0,len(nums)):
            ls = 0
            rs = 0
            for a in range(0,i):
                ls += nums[a] 
            for b in range(i+1, len(nums)):
                rs += nums[b]
            print(ls)
            print(rs)
            if (ls == rs):
                return(i)
        return(-1)
            
            