class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        myarray = []
        for i in range(2):
            for n in nums:
                myarray.append(n)
        return myarray


        