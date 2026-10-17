class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        returnarr = []
        l, r = 0, 0
        for i in range(len(nums)-1):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            l = i + 1
            r = len(nums)-1
            while l < r:
                if (nums[l] + nums[r] > target):
                    r -= 1
                elif (nums[l] + nums[r] < target):
                    l += 1
                else:
                    returnarr.append([nums[l], nums[r], -target])
                    r -= 1
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                
        return(returnarr)
                
                