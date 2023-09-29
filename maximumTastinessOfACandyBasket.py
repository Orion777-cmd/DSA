class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        price.sort()
       
        res = float('-inf')
        leng = len(price)
        

        def isValid(diff):
            count = 1
            curr_min = price[0]
            for i in range(1, leng):
                if price[i] - curr_min >= diff:
                    count += 1
                    curr_min = price[i]
                    if count == k:
                        return True
            return False

        lo = 0
        high = price[leng-1] - price[0]
        while lo <= high:
            mid = (lo + high)//2
            if isValid(mid):
                lo = mid+1
            else:
                high = mid-1
        return lo -1



        return res
