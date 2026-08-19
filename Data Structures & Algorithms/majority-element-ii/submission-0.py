class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        myhash = {}
        result = []
        minimum = len(nums) // 3
        for num in nums:
            if num in myhash:
                myhash[num] += 1
            else:
                myhash[num] = 1
        for num in myhash:
            if myhash[num] > minimum:
                result.append(num)
        return(result)
