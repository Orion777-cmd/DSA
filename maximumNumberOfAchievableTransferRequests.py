class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:

        res = [0] * n
        ans = 0
        
        def backtrack(start, requests, res, n, count):
            nonlocal ans
            if start == len(requests):
                if not all(_ == 0 for _ in res):
                    return 
            
                ans = max(ans, count)
                return

            res[requests[start][0]] -= 1
            res[requests[start][1]] += 1
            backtrack(start+1, requests, res, n, count+1)

            res[requests[start][0]] += 1
            res[requests[start][1]] -= 1
            backtrack(start+1, requests, res, n, count)

        backtrack(0, requests, res, n, 0)

        return ans

        
