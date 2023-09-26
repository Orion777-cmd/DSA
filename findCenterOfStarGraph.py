class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        
        def buildGraph(edges):
            graph =  {}
            for edge in edges:
                node1, node2 = edge
                if not node1 in graph:
                    graph[node1]= []
                if not node2 in graph:
                    graph[node2]=[]
                graph[node1].append(node2)
                graph[node2].append(node1)
               
            return graph
        graph = buildGraph(edges) 
        tot = len(graph.keys())
        for i in graph.keys():
            if len(graph[i]) == tot -1:
                return i


       
