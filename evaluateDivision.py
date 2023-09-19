class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        #build an adjecency list for the equations
        graph = defaultdict(list)
        for i, vals in enumerate(equations):
            num, den = vals
            graph[num].append([den, values[i]])
            graph[den].append([num, 1/ values[i]])
        
        def bfs(numerator, denominator):
            if numerator not in graph or denominator not in graph:
                return -1.0
            
            queue, visited = deque(), set()
            queue.append([numerator, 1])

            while queue:
                node, weight = queue.popleft()
                if node == denominator:
                    return weight
                
                for neighbor, current_weight in graph[node]:
                    if neighbor not in visited:
                        queue.append([neighbor, weight * current_weight])
                        visited.add(neighbor)
            return -1.0

        return [bfs(query[0], query[1]) for query in queries]

        
