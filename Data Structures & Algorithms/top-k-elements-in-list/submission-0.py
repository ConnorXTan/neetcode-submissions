class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict = {}
        myarr = [[] for i in range(len(nums) + 1)]
        for num in nums:
            mydict[num] = 1 + mydict.get(num, 0)
        for n, c in mydict.items():
            myarr[c].append(n)
        
        returned = []
        for n in range(len(myarr)-1, 0, -1):
            for i in myarr[n]:
                returned.append(i)
                if (len(returned) == k):
                    return(returned)
        