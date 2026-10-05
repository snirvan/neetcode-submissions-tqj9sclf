class UnionFind:
    
    def __init__(self, n: int):
        #track parents
        self.par = {}
        #track height
        self.height = {}
        #track components
        self.components = 0

        self.components = n

        for i in range(0,n):
            self.par[i] = i
            self.height[i] = 0
        

    def find(self, x: int) -> int:
        # check if same parents
        p = self.par[x]
        while p != self.par[p]:
        # compress parent to grandparent 
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    def isSameComponent(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)



    def union(self, x: int, y: int) -> bool:
        if self.isSameComponent(x,y):
            return False
        
        x_root = self.find(x)
        y_root = self.find(y)

        if self.height[x_root] > self.height[y_root]:
            self.par[y_root] = x_root
        if self.height[y_root] > self.height[x_root]:
            self.par[x_root] = y_root
        else:
            self.par[x_root] = y_root
            self.height[x_root] += 1

        self.components -= 1
        return True

        

    def getNumComponents(self) -> int:
        return self.components

