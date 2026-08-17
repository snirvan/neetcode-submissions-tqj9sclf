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
        popped = self.arr.pop()
        if self.min[-1] == popped:
            self.min.pop()
        

    def top(self) -> int:
        return self.arr[-1]
        

    def getMin(self) -> int:
        return self.min[-1]
        

#1,2,0
# 1,0

# push: always push to arr
# only push to min if if min is empty or if 