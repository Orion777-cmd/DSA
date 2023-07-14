class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        min_ = float('-inf')
        for i in range(len(nums)-1, -1, -1):
            if nums[i] < min_:
                return True
            else:
                while stack and stack[-1] < nums[i]:
                    min_ = stack.pop()
            stack.append(nums[i])
        return False
