class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        i1 = i2 = 0
        bigmax = 0
        while l < r:
            maxt = (r - l) * min(heights[l], heights[r])
            if bigmax < maxt:
                bigmax = maxt
            if heights[l] < heights[r]:
                l += 1
                continue
            if heights[r] < heights[l]:
                r -= 1
                continue
            l += 1
            r -= 1
        return bigmax
