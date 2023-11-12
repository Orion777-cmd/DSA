class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target: return 0
        graph = defaultdict(list)
        for i, nodes in enumerate(routes):
            for node in nodes:
                graph[node].append(i)
       
        bus_count = 1
        queue = deque()
        visited = set()
        for route in graph[source]:
            queue.append(route)
            visited.add(route)
        
        while queue:
            size = len(queue)
            for _ in range(size):
                route = queue.popleft()
                for stop in routes[route]:
                    if stop == target:
                        return bus_count
                    for neighbor in graph[stop]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
            bus_count += 1
        return -1
