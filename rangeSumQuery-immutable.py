class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.tot = 0
    def sumRange(self, left: int, right: int) -> int:
        self.tot = sum(self.nums[left:right+1])
        return self.tot


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
