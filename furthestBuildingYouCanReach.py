class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        heap = []
        for i in range(1, len(heights)):
            height_difference = heights[i] - heights[i-1]
            if height_difference > 0:
                heapq.heappush(heap, height_difference)
            
            if len(heap) > ladders:
                bricks -= heapq.heappop(heap)
            if bricks < 0:
                return i-1
        return len(heights)-1
        
