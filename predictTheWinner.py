class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        # using minmax algorithm
        def max_score(nums, i, j, turn):
            
            if i == j:
                return nums[i] * turn
            score_left = nums[i] * turn + max_score(nums, i + 1, j, -turn)
            score_right = nums[j] * turn + max_score(nums, i, j - 1, -turn)
           
            return max(score_left * turn, score_right * turn) * turn
        return max_score(nums, 0, len(nums) - 1, 1) >= 0
