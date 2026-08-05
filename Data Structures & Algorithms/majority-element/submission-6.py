class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if (len(nums) % 2 == 1):
            middle = round(len(nums) / 2) 
            if (middle > len(nums) / 2):
                middle -= 1
        else:
            middle = len(nums) / 2
        nums.sort()
        print(middle)
        return(nums[int(middle)])