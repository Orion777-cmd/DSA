class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        res = []
        count = Counter(nums)
        max_rows = 0
        for key,val in count.items():
            max_rows = max(max_rows, val)
        
        for i in range(max_rows):
            temp = []
            for key, val in count.items():
                if val >= i+1:
                    temp.append(key)
            if temp: res.append(temp)
        return res
