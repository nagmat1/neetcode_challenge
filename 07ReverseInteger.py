class Solution:
    def reverse(self, x: int) -> int:
        MIN = -1 * 2 ** 31
        MAX = 2 ** 31 -1
        if x >= 0 :  
            neg = False
        else : 
            neg = True
        x =abs(x)
        res = 0 
        while x :
            if 10*res + x % 10 > MAX :
                return 0
            res = 10*res + x % 10
            x = x // 10
        if neg : 
            return -1*res
        else: 
            return res
