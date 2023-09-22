class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            x, y = point
            heapq.heappush(heap, ((x**2 + y ** 2)**0.5,x,y))
        
        # heapq.heapify(heap)
        # print(heap)
        
        res = []
        while heap and k > 0:
            # print(heap)
            _,x,y = heapq.heappop(heap)
            
            res.append([x,y])
            k -= 1
        return res

