class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * 3
        for num in nums:
            count[num] += 1
        a = 0
        for i in range(3):
            while count[i] > 0:
                nums[a] = i
                count[i] -= 1
                a += 1


