class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        lesser = [0]*len(nums)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    lesser[i] += 1
        return lesser
        
