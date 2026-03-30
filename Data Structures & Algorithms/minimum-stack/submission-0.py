class MinStack:

    def __init__(self):
        self.st1 = []

    def push(self, val: int) -> None:
        self.st1.append(val)

    def pop(self) -> None:
        self.st1.pop()

    def top(self) -> int:
        return self.st1[-1]

    def getMin(self) -> int:
        tmp = []
        mini = self.st1[-1]
        for i in range(len(self.st1)):
            mini = min(mini, self.st1[-1])
            tmp.append(self.st1.pop())

        for i in range(len(tmp)):
            self.st1.append(tmp.pop())
        
        return mini
        
