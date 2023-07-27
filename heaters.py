class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()

        def binarySearch(house):
            left, right = 0, len(heaters)
            minDist = float('inf')
            while left < right:
                mid = (left + right)//2
                minDist = min(minDist, abs(heaters[mid]-house))
                if heaters[mid] < house:
                    left = mid+1
                else:
                    right = mid
            return minDist
        
        res = []
        for house in houses:
            res.append(binarySearch(house))
        return max(res)
