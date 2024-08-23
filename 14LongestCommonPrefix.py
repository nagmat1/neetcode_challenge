class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = "" 
        strs = sorted(strs)
        if len(strs[0])== 0 : 
            return ""
        elif len(strs)==1 : 
            return strs[0]
        for i in range(len(strs[0])): 
            if strs[0][i]!=strs[-1][i]:
                return pref
            pref = pref+strs[0][i]
        return pref
