class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        time = 0
        heap = [-cnt for cnt in count.values() ]

        heapq.heapify(heap)
        # print(heap)
        queue = deque()

        while queue or heap:
            time += 1
            # print("heap: ", heap, "queue: ", queue)
            if heap:
                item = heapq.heappop(heap) + 1
                # print(item)
                if item != 0:
                    queue.append((item, time + n))
            
            if queue and queue[0][1] == time:
                heapq.heappush(heap, queue.popleft()[0])
        
        return time
        
