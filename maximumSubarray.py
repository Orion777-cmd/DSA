class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_ = -inf
        running = 0
        for num in nums:
            running += num
            if running > max_:
                max_ = running
            if running < 0:
                running = 0
        return max_
