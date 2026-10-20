class MinStack:

    def __init__(self):
        self.arr = []
        self.minarr = []

    def push(self, val: int) -> None:
        self.arr.append(val)
        if not self.minarr or val <= self.minarr[-1]:
            self.minarr.append(val)

    def pop(self) -> None:
        val = self.arr.pop()
        if val == self.minarr[-1]:
            self.minarr.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.minarr[-1]
        

        
