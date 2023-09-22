class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        heap = []
        events.sort()
        day = 0
        attended = 0
        i = 0

        # print(events)
        while i < len(events) or heap:
            if not heap:
                day = events[i][0]
            
            while i < len(events) and events[i][0] <= day:
                heapq.heappush(heap, events[i][1])
                i += 1
            # print(heap)
            if heap:
                heapq.heappop(heap)
                attended += 1
                day += 1
            
            while heap and heap[0] < day:
                heapq.heappop(heap)
        
        return attended
