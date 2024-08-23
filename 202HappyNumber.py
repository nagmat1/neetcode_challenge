class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set() 
        while n not in visit: 
            visit.add(n)
            res = 0
            while n>0:
                res = res + (n % 10)**2
                n = n // 10
            n = res 
            if n == 1 : 
                return True 
        return False
