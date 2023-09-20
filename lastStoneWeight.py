import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap,-stone)
        while len(heap) >= 2:
            x = -heapq.heappop(heap)
            y = - heapq.heappop(heap)
            if x == y:
                continue
            new = x - y
            if x > 0:
                heapq.heappush(heap, -new)
            else:
                heapq.heappush(heap, new)
        return -heap[0] if heap else 0
        
