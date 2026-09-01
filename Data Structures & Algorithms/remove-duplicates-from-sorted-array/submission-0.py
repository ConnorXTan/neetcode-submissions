class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter = 1
        num = 1
        first = nums[0]
        while num < (len(nums)):
            if nums[num] != first:
                counter += 1
                first = nums[num]
                num += 1
            else:
                nums.pop(num)

        return(counter)
