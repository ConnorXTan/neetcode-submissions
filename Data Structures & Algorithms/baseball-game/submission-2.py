class Solution:
    def calPoints(self, operations: List[str]) -> int:
        myarr = []
        listindex = 0
        for i in range(len(operations)):
            if (operations[i] == "+"):
                myarr.append(int(myarr[listindex - 1]) + int(myarr[listindex - 2]))
                listindex += 1
            elif (operations[i] == "C"):
                myarr.pop()
                listindex -= 1
            elif (operations[i] == "D"):
                myarr.append(int(myarr[listindex - 1]) * 2)
                listindex += 1
            else:
                myarr.append(int(operations[i]))
                listindex += 1
        return sum(myarr)
        

