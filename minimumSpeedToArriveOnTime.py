class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
    
        length = len(dist)
        min_speed = float('inf')
       
        def isPossible(speed):
            temp_time = 0

            for i in range(length - 1):
                temp_time += math.ceil(dist[i] / speed)
            
            temp_time += dist[length - 1] / speed

            return temp_time <= hour
        lo = 1
        high = 10 ** 7

        while lo <= high:
            mid = lo + (high -lo)//2
            
            if isPossible(mid):
                min_speed = min(min_speed, mid)
                high = mid -1
            else:
                lo = mid +1
            
        return min_speed if isinstance(min_speed, int) else -1
