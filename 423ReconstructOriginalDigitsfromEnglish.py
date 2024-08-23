class Solution:
    def originalDigits(self, s: str) -> str:
        digits = {} 
        cnt = Counter(s)
        digits[0] = cnt['z']
        digits[2] = cnt['w']
        digits[4] = cnt['u']
        digits[5] = cnt['f']-digits[4]
        digits[6] = cnt['x']
        digits[8] = cnt['g']
        digits[7] = cnt['s']-digits[6]
        digits[9] = cnt['i']-digits[8]-digits[6]-digits[5]
        digits[3] = cnt['h']-digits[8]
        digits[1] = cnt['o']-digits[2]-digits[4]-digits[0]
        res = "" 
        for i in range(10): 
            res = res + str(i)*digits[i]
        return res
