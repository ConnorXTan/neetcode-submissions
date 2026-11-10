class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        arraynum = None
        for i in range(len(matrix)):
            if matrix[i][-1] >= target:
                arraynum = i
                break
        if (arraynum == None): return False
        else:
            l = 0
            r = len(matrix[arraynum])-1
            print(arraynum)
            while l <= r:
                m = (l + r) // 2
                if target < matrix[arraynum][m]:
                    r = m - 1
                elif target > matrix[arraynum][m]:
                    l = m + 1
                else:
                    return True
            return False