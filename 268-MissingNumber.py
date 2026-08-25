class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        expected_total = ((n+1)*n)//2
        actual_total = sum(nums)
        return expected_total - actual_total