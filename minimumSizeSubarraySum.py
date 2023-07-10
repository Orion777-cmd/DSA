class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        low, high = 1, len(nums) + 1
        while (low < high):
            
            mid = (low + high)//2
            
            if self.slidingWin(target, nums, mid):
                high = mid
            else:
                low = mid + 1
                
        if self.slidingWin(target, nums, low): return low
        else: return 0
            
        
        
    
    def slidingWin(self, target, nums, k):
        curSum = 0
        maxSum = 0
        l = 0
        for i in range(len(nums)):
            curSum += nums[i]
            if i > k - 1:
                curSum -= nums[l]
                l += 1
                
            maxSum = max(curSum, maxSum)
            
        return (maxSum >= target)
