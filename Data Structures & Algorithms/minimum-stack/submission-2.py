class MinStack:
    #Optimal Solution with O(1) TC for all ops
    def __init__(self):
        self.st = []
        self.minSt = []

    def push(self, val: int) -> None:
        self.st.append(val)
        val = min(val, self.minSt[-1] if self.minSt else val)
        self.minSt.append(val)

    def pop(self) -> None:
        self.st.pop()
        self.minSt.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.minSt[-1]
    
    #Solution with O(n) TC for getMin op and O(1) for other ops
    # def __init__(self):
    #     self.st1 = []

    # def push(self, val: int) -> None:
    #     self.st1.append(val)

    # def pop(self) -> None:
    #     self.st1.pop()

    # def top(self) -> int:
    #     return self.st1[-1]

    # def getMin(self) -> int:
    #     tmp = []
    #     mini = self.st1[-1]
    #     for i in range(len(self.st1)):
    #         mini = min(mini, self.st1[-1])
    #         tmp.append(self.st1.pop())

    #     for i in range(len(tmp)):
    #         self.st1.append(tmp.pop())
        
    #     return mini
        
