class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0 
        diff = float('inf')
        for i in range(len(nums)-1): 
            start = i+1
            end = len(nums)-1
            while start<end : 
                sum1 = nums[i]+nums[start]+nums[end]
                if sum1 ==target : 
                    return target 
                elif abs(target-sum1)<=diff: 
                    diff =abs(target-sum1)
                    res = sum1 
                if sum1 > target : 
                    end=end-1 
                else: 
                    start = start +1            
        return res                 
