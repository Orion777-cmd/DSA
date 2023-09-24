class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        @lru_cache(None)
        def dfs(node):
            if node not in graph:
                return node
            min_ = node
            for neighbour in graph[node]:
                val = dfs(neighbour)
                if quiet[min_] > quiet[val]:
                    min_ = val 
            return min_  
        n = len(quiet)
        graph = defaultdict(list)
        for more, less in richer:
            graph[less].append(more)
        return list(map(dfs , range(n)))
        
