class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph  = defaultdict(list)
        room = [False] * len(rooms)

        for i, value in enumerate(rooms):
            for val in value:
                graph[i].append(val)
        
        def dfs(door):

            if room[door] == True:
                return
            room[door] = True
            for keys in graph[door]:
                dfs(keys)
        dfs(0)
        return False not in room
