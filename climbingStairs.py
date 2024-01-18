class Solution:
    def climbStairs(self, n: int) -> int:
        last = 1
        second_last = 0
        for i in range( n):
            second_last, last = last, second_last + last
        return last
