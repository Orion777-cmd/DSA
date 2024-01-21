class Solution:
    def rob(self, nums: List[int]) -> int:
        
        def robHouse(i: int) -> int:
            if i >= len(nums):
                return 0
            
            if i in memo:
                return memo[i]

            rob_current = nums[i] + robHouse(i+2)
            skip_current = robHouse(i+1)
            memo[i] = max(rob_current, skip_current)
            return memo[i]
        memo = {}

        return robHouse(0)
