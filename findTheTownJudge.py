class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustMap = {i:[] for i in range(1, n+1)}
        trusteeMap = {i:[] for i in range(1, n+1)}

        for t in trust:
            trustMap[t[1]].append(t[0])
            trusteeMap[t[0]].append(t[1])
        
        for i, jList in trustMap.items():
            if len(jList) == (n - 1) and len(trusteeMap[i]) == 0:
                return i

        return -1
