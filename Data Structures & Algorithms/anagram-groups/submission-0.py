class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = {}
        for string in strs:
            stringlist = sorted(string)
            sortedstring = "".join(stringlist)
            if sortedstring in mydict:
                mydict[sortedstring].append(string)
            else:
                mydict[sortedstring] = []
                mydict[sortedstring].append(string)
        return(list(mydict.values()))