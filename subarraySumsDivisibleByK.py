class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum =  [nums[0]]
        remainder = Counter(map(lambda x: x  % k , accumulate(nums)))

        subarrays = 0
        for remain in remainder:
            subarrays += remainder[remain] * (remainder[remain]-1) // 2
        subarrays += remainder[0]
        return subarrays
