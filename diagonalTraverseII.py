class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        """
        0,0
        1,0     0,1
        2,0     1,1     0,2
        2,1     1,2
        2,2       
        
        """
        queue = deque([(0, 0)])
        res = []
        while queue:
            row, col = queue.popleft()
            res.append(nums[row][col])
            if col == 0 and row + 1 < len(nums):
                queue.append((row+1, col))
            if col + 1 < len(nums[row]):
                queue.append((row, col + 1))
        return res
