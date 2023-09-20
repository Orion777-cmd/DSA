import heapq
class Solution:
    def largestInteger(self, num: int) -> int:
        odd = []
        even = []
        for nu in str(num):
            if int(nu) % 2 == 0:
                heapq.heappush(even, -int(nu))
            else:
                heapq.heappush(odd, -int(nu))
    
        ans = ''
        for n in str(num):
            if int(n) %  2 == 0 and even:
                ans += str(-even.pop(0))
            else:
                if odd:
                    ans += str(-odd.pop(0))
        
        return int(ans)
