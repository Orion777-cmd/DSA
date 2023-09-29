class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        candies = [i for i, c in enumerate(s) if  c =="|"]

        def binarySearch(num):
            lo = 0
            hi = len(candies)-1

            while lo <= hi:
                mid = (lo + hi) //2
                if candies[mid] < num:
                    lo = mid +1
                else:
                    hi = mid-1
            return lo

        ans = []
        for from_, to_ in queries:
            left, right = binarySearch(from_), binarySearch(to_+1)-1
            ans.append(candies[right]-candies[left] - (right-left)if left < right else 0)  
        return ans


######### using Prefix Sum #################
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        prefix_sum = [0]
        candles = []
        for i, ch in enumerate(s):
            if ch == '|': candles.append(i)
            if ch == '|': prefix_sum.append(prefix_sum[-1])
            else: prefix_sum.append(prefix_sum[-1] + 1)
        
        ans = []
        for from_, to_ in queries:
            lo = bisect_left(candles, from_)
            hi = bisect_right(candles, to_)-1
            if lo <= hi:
                ans.append(prefix_sum[candles[hi]+1] - prefix_sum[candles[lo]])
            else:
                ans.append(0)
        return ans
            
