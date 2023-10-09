class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        def binary_search(nums, target, left):
            lo, hi  = 0, len(nums)-1
            index = -1
            while lo <= hi:
                mid = (lo + hi)//2
                if nums[mid] == target:
                    index = mid
                    if left:
                        hi = mid -1
                    else:
                        lo = mid + 1
                elif nums[mid] < target:
                    lo = mid + 1
                else:
                    hi = mid-1
            return index
        left = binary_search(nums, target, left = True)
        right = binary_search(nums, target, left =False)

        return [left, right]
    
            
