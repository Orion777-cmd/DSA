class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res, temp = [], []

        def recursion(start, target,k):
            if k != 2:
                for i in range(start, len(nums)-k+1):
                    if i > start and nums[i] == nums[i-1]:
                        continue
                    temp.append(nums[i])
                    recursion(i+1, target-nums[i], k-1)
                    temp.pop()
                return 
            
            left, right = start, len(nums)-1
            while left < right:
                if nums[left] + nums[right] > target:
                    right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    res.append(temp + [nums[left],nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
        recursion(0, target, 4)
        return res            
                
                
            


        
