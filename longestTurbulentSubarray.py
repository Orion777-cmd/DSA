class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        i, j = 0, 0
        res = 1
        length = len(arr)
        while j < length:
            while i < length -1 and arr[i] == arr[i+1]:
                i += 1
            while j < length-1 and (arr[j-1] < arr[j] > arr[j+1] or arr[j-1] > arr[j] < arr[j+1]):
                j+= 1
            res = max(res, j-i+1)
            i = j
            j += 1
        return res
