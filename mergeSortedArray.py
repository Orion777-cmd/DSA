class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        left = right = 0
        while left < m and right < n:
            
            if nums1[left]<=nums2[right]:
                
                left += 1
            else:
                while nums1[left] >= nums2[right] and m < m+n:
                    
                    nums1[left],nums2[right] = nums2[right],nums1[left]
                    if left < m -1:
                        left += 1
                    else :
                        nums1[m] = nums2[right]
                        m += 1
                        left = 0
                        break
                
                right += 1
            
        while m < m +n and right < n:
            nums1[m] = nums2[right]
            m += 1
            right += 1
        
