class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        divider = 10 ** 9 + 7
        stack = []
        res = [0] * len(arr)
        prev = [-1] *  len(arr)

        for i in range(len(arr)):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                prev[i] = stack[-1]
            stack.append(i)
        tot = 0
        for i in range(len(arr)):
            res[i] = ((res[prev[i]] if prev[i] != -1 else 0) + (i-prev[i]) * arr[i]) 
            tot += res[i] % divider
        return tot % divider
