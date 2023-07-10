class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        i, j = 0, 0
        res = float('-inf')
        temp = 0
        while j < len(nums):
            if j - i == k:
                avg = temp / k
                res = max(res, avg)
                temp -= nums[i]
                i += 1
            else:
                temp += nums[j]
                j += 1
        return max(res, temp/k) if j-i ==k else res
