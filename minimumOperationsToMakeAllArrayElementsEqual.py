class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix_sum = [nums[0]]
        min_operations = []
        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[-1] + nums[i])
        
        for query in queries:
            left = 0
            right = len(nums) - 1
            left_index = -2 
                   
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] > query:
                    right = mid - 1
                elif nums[mid] < query:
                    left = mid + 1
                else:
                    left_index = mid
                    right = mid - 1     

            if left_index == -2:
                left_index = min(left, right)
           
            if left_index == -1:
                min_operations.append(prefix_sum[-1] - (len(nums))*query)
            else:
                min_operations.append((left_index+1)*query - prefix_sum[left_index] + prefix_sum[-1] - prefix_sum[left_index] - (len(nums) -1 - left_index)*query)
            
        return min_operations
