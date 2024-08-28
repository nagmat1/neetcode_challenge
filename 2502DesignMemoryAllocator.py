class Allocator:

    def __init__(self, n: int):
        self.mem = [False]*n
        self.N = n
        self.memP = [0]*self.N

    def allocate(self, size: int, mID: int) -> int:
        #print(f"memP = {self.memP} mem= {self.mem}")
        i = 0 
        while i < self.N : 
            if self.mem[i]==False: 
                if self.N-i<size : 
                    return -1
                bool1 = True
                for j in range(i,i+size): 
                    bool1 = bool1 and self.mem[j]==False
                    if not bool1 : 
                        i = j
                        break
                if bool1 : 
                    for j in range(i,i+size): 
                        self.memP[j] = mID 
                        self.mem[j]  = True
                    return i
            i = i+1
        return -1
                    

    def free(self, mID: int) -> int:
        #print(f"FmemP = {self.memP} mem= {self.mem}")
        count = 0 
        for i in range(self.N): 
            if self.memP[i]==mID : 
                self.memP[i] = 0 
                self.mem[i]  = False
                count = count + 1
        return count
        
        


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)
