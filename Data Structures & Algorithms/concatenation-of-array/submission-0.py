class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        mylist = []
        mylist2 = []
        for i in range(len(nums)):
            mylist.append(nums[i])
            mylist2.append(nums[i])
        return(mylist+mylist2)


        