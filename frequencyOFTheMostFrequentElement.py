class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        prefix_sum = [nums[0]]
        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[-1] + nums[i])
        
        def binary_search(ind):
            target = nums[i]
            lo = 0
            hi = ind
            best = ind
            
            while lo <= hi:
                mid = (lo + hi) // 2
                count = ind - mid +1
                final_sum = count * target
                original_sum = prefix_sum[ind] - prefix_sum[mid] + nums[mid]
                operation_required = final_sum - original_sum
                if operation_required > k:
                    lo = mid +1
                else:
                    best = mid
                    hi = mid-1
            return ind - best +1
            
        ans = 0
        for i in range(len(nums)):
            ans = max(ans, binary_search(i))
        return ans
