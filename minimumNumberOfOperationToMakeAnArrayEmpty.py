class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = Counter(nums)
        minOp = 0
        for key, val in count.items():
            if val == 1:
                return -1
            minOp += ceil(val /3)
        return minOp
