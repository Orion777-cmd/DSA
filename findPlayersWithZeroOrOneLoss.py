class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        notLoose = []
        oneLoose = []
        res =[]
        graph = defaultdict(list)
        players = set()
        for match in matches:
            if match[0] not in players:
                players.add(match[0])
            if match[1] not in players:
                players.add(match[1])
            graph[match[1]].append(match[0])
        for num in players:
            if len(graph[num]) == 0:
                notLoose.append(num)
            if len(graph[num])==1:
                oneLoose.append(num)
        notLoose.sort()
        oneLoose.sort()
        res.append(notLoose)
        res.append(oneLoose)
        return res
