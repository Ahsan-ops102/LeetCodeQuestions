class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        
        ways_prev1 = 1
        ways_prev2 = 1

        for i in range(2, n+1):
            ways = ways_prev1 + ways_prev2
            ways_prev1 = ways_prev2
            ways_prev2 = ways
        return ways