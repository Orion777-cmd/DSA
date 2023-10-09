class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        min_sum , max_sum = 0, 0
        stack = []
        for i in range(len(nums)+1):
            while stack and (i == len(nums) or nums[stack[-1] ]> nums[i]):
                temp = stack.pop()
                prev_small = stack[-1] if stack else -1
                min_sum += nums[temp] * (i -temp) * (temp-prev_small)
            stack.append(i)
        
        stack = []
        for i in range(len(nums)+1):
            while stack and (i == len(nums) or nums[stack[-1] ] < nums[i]):
                temp = stack.pop()
                prev_large = stack[-1] if stack else -1
                max_sum += nums[temp] * (i -temp) * (temp-prev_large)
            stack.append(i)
       
        return max_sum - min_sum
