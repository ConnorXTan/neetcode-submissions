class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        myvalues = []
        repeated = 0
        missing = 0
        for i in range(len(grid)):
            for a in range(len(grid[i])):
                if grid[i][a] in myvalues:
                    repeated = grid[i][a]
                else:
                    myvalues.append(grid[i][a])
        myvalues.sort()
        print(myvalues)
        for b in range(len(myvalues)-1):
            if ((myvalues[b+1] - myvalues[b]) != 1):
                missing = myvalues[b] + 1
                break
            if myvalues[len(myvalues)-1] == len(myvalues):
                missing = len(myvalues)+1
            else:
                missing = 1

        
        return([repeated, missing])
