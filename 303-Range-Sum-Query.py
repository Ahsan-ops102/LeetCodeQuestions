class NumArray:

    def __init__(self, nums: List[int]):
        # prefix[i] stores the sum of elements from nums[0] to nums[i - 1]
        self.prefix = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.prefix[i + 1] = self.prefix[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        # Sum of nums[left ... right] = prefix[right + 1] - prefix[left]
        return self.prefix[right + 1] - self.prefix[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)