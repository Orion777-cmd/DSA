import heapq
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        weak_list = []
        dict_ = defaultdict(int)
        for i in range(len(mat)):
            soldier = 0
            for peop in mat[i]:
                if peop == 1:
                    soldier += 1
            dict_[i] = soldier
        
        dict_ = sorted(dict_.items(), key = lambda x :x[1])
        print(dict_)
        res = []
        for j in range(k):
            res.append(dict_[j][0])
        
        return res


        
