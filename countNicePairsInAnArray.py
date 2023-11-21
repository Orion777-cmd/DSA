class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        modulo = 10 ** 9 + 7
        dict_ = defaultdict(int)
        for num in nums:
            dict_[num-int(str(num)[::-1])] += 1
            
        ans = 0
        for key, val in dict_.items():
            if val > 1:
                ans += math.comb(val, 2) % modulo
        
        return ans % modulo
