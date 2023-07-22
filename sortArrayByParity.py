class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        even = [num for num in nums if num % 2 ==0]
        odd = [num for num in nums if num % 2 != 0]

        even.extend(odd)
        return even
