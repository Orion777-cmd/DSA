
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        def buildGraph(graph):
            adjecent = {i:[] for i in range(len(graph))}
            for i in range(len(graph)):
                for j in graph[i]:
                    adjecent[i].append(j)
            return  adjecent

        adjecent = buildGraph(graph)
        # print(adjecent)

        res = []
        def dfs(node , path):
            
            if path[-1] == len(adjecent)-1:
                res.append(path)
                return
            
            for neighbor in adjecent[node]:
                temp = path.copy()
                temp.append(neighbor)
                dfs(neighbor, temp)


        dfs(0,[0])
        return res
