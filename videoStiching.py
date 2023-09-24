class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        clips.sort(reverse =True)
   
        heap = []
        min_clip = 0
        i = 0

        while i < time:
            while clips and clips[-1][0] <= i:
                start, end = clips.pop()
                heapq.heappush(heap, -end)
            
            if not heap or -heap[0] <= i: return -1
            current = -heapq.heappop(heap)
            i = current
            
            min_clip += 1
            
        return min_clip
        
            
