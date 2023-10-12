class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        left, right = 0, mountain_arr.length() - 1
        while left < right:
            mid = (left + right) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                left = mid + 1
            else:
                right = mid

        peak = left

        left, right = 0, peak
        while left <= right:
            mid = (left + right) // 2
            if mountain_arr.get(mid) < target:
                left = mid + 1
            elif mountain_arr.get(mid) > target:
                right = mid - 1
            else:
                return mid

        left, right = peak, mountain_arr.length() - 1
        while left <= right:
            mid = (left + right) // 2
            if mountain_arr.get(mid) > target:
                left = mid + 1
            elif mountain_arr.get(mid) < target:
                right = mid - 1
            else:
                return mid

        return -1
