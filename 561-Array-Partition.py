class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        values = []

        for i in range(len(nums)):
            if i % 2 == 0:
                values.append(nums[i])
        return sum(values)
                
            