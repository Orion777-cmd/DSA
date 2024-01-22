class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        """
        1, 2, 3, 4 ,5, 6 , 7, 8, 9, 10
        sum = 10 * 11 / 2 = 55

        1, 2, 2,3, 4, 5 , 7, 8, 9 , 10
        51-2 = 49

        55 - 49 = 6 -> missed number
        
        """
        current_sum = sum(nums)
        target_sum = (len(nums)+1) * len(nums) // 2

        count = Counter(nums)
        for key, val in count.items():
            if val == 2:
                break
        return [key, target_sum - current_sum+key]
