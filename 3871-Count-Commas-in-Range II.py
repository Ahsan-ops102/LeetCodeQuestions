class Solution:
    def countCommas(self, n: int) -> int:
        count = 0
        threshold = 1000

        while threshold <= n:
            count += n-threshold + 1

            threshold = threshold * 1000
        return count
