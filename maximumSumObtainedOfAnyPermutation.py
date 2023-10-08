class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        
        prefixSum = [0 for _ in range(len(nums))]
        for start, end in requests:
            prefixSum[start] += 1
            if end < len(nums)-1:
                prefixSum[end+1] -= 1
        
        for i in range(1,len(nums)):
            prefixSum[i] += prefixSum[i-1]
    
        prefixSum.sort()
        nums.sort()

        modulo = 10 ** 9 + 7
        res = 0
        for i in range(len(nums)-1, -1, -1):
            res += (prefixSum[i] * nums[i]) % modulo
            res %= modulo

        return int(res % modulo) 
