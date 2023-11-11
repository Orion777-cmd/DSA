class Graph:

    def __init__(self, n: int, edges: List[List[int]]):
        self.graph = defaultdict(list)
        for from_, to_, cost in edges:
            self.graph[from_].append((to_, cost))
            
        

    def addEdge(self, edge: List[int]) -> None:
        from_, to_, cost = edge
        self.graph[from_].append((to_, cost))

    def shortestPath(self, node1: int, node2: int) -> int:
        queue = [(0, node1)]
        
        visited = set()
        while queue:
            cost, to_ = heappop(queue)
            
            visited.add(to_)
            if to_ == node2:
                return cost

            for neighbor in self.graph[to_]:
                neigh, current_cost = neighbor
                if neigh not in visited:
                    heappush(queue,(current_cost + cost, neigh) )
        return -1

# Your Graph object will be instantiated and called as such:
# obj = Graph(n, edges)
# obj.addEdge(edge)
# param_2 = obj.shortestPath(node1,node2)
