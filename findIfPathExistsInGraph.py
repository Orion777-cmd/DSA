class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for edge in edges:
            src, dst = edge
            graph[src].append(dst)
            graph[dst].append(src)
       
        queue = [source]
        visited = set()
        while queue:
            current = queue.pop()
         
            if current == destination:
                return True
            visited.add(current)
            neighbors = graph[current]
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
               
        return False
