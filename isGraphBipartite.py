class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        length = len(graph)
        res = [-1] * length
        for i in range(length):
            if res[i] != -1:
                continue
            queue = deque()
            queue.append((i, 0))
            while queue:
                current, color = queue.popleft()
                if res[current] == -1:
                    res[current] = color
                    for node in graph[current]:
                        queue.append((node,color^1))
                if res[current] != color:
                    return False
        return True
