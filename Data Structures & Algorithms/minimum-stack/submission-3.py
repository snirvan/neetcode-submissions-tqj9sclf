class MinStack:

    def __init__(self):
        self.arr = []
        self.min = []
        

    def push(self, val: int) -> None:
        self.arr.append(val)
        if len(self.min) == 0:
            self.min.append(val)
        elif val <= self.min[-1]:
            self.min.append(val)

    def pop(self) -> None:
        x = self.arr.pop()
        if x == self.min[-1]:
            self.min.pop()
        

    def top(self) -> int:
        return self.arr[-1]
        

    def getMin(self) -> int:
        return self.min[-1]
        
