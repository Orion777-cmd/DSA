class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = [_ for _ in range(1, n+1)]
        combinations = []

        def backtracking(i, combination):
            if len(combination) == k:
                combinations.append(combination[:])
                return 
            if i >=n:
                return
            combination.append(nums[i])
            backtracking(i+1, combination)
            combination.pop()

            backtracking(i+1, combination)
        backtracking(0, [])
        return combinations
