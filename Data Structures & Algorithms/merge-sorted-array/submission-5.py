class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #1 2 3 0 0 0
        #2 5 6
        #
        index1, index2 = 0, 0
        while index1 < m + index2:
            if index2 < n:
                if nums1[index1] >= nums2[index2]:
                    nums1.insert(index1, nums2[index2])
                    nums1.pop()
                    index2 += 1
            index1 += 1
        print(nums1,index1)
        for i in range(index2, len(nums2)):
            nums1[index1] = nums2[i]
            index1 += 1
            
