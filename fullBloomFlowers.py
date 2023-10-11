class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        people = [(p,i) for i,p in enumerate(people)]
        start = [f[0] for f in flowers]
        end = [f[1] for f in flowers]
        heapq.heapify(start)
        heapq.heapify(end)
        res = [0 for _ in range(len(people))]
        count = 0
        for pep, i in sorted(people):
            while start and start[0] <= pep:
                heapq.heappop(start)
                count += 1
            while end and end[0] < pep:
                heapq.heappop(end)
                count -= 1
            res[i] = count
        
        return res

################## relative optimal Solution ###########################
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        people = [(p,i) for i,p in enumerate(people)]
        
        end = []
        flowers = sorted(flowers)
        res = [0 for _ in range(len(people))]
        j = 0
        for pep, i in sorted(people):
            while j < len(flowers) and flowers[j][0] <= pep:
                heapq.heappush(end, flowers[j][1])
                j += 1
            while end and end[0] < pep:
                heapq.heappop(end)
            
            res[i] = len(end)
        
        return res

