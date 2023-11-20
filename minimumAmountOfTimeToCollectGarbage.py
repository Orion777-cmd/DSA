class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        total_time =0
        travel_prefix = [0]
        for i in range(len(travel)):
            travel_prefix.append(travel_prefix[-1] + travel[i])
        type_garbage = ["M", "P", "G"]
        for garb in type_garbage:
            temp = 0
            indice = -1
            for i in range(len(garbage)):
                cur = Counter(garbage[i])
                count = cur[garb]
                if count == 0:   
                    continue
                indice = i
                temp += count
            if indice != -1:
                temp += travel_prefix[indice]
            total_time += temp
        return total_time
