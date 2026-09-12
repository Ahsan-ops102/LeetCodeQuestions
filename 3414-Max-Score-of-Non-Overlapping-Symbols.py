import bisect
from typing import List

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        
        # 1. Annotate intervals with their original 0-based indices
        annotated_intervals = []
        for i in range(n):
            annotated_intervals.append((intervals[i][0], intervals[i][1], intervals[i][2], i))
            
        # 2. Sort intervals by their ending point `r_i` in ascending order.
        # Ties are broken by `l_i` then `orig_id`.
        annotated_intervals.sort(key=lambda x: (x[1], x[0], x[3]))
        
        # Array specifically built mapping the sorted r_i values for O(log N) binary searches
        R = [0] * (n + 1)
        for i in range(n):
            R[i + 1] = annotated_intervals[i][1]
            
        # 3. Initialize the dynamic programming table
        # dp[i][k] will record a tuple: (max_weight, min_lexicographical_tuple)
        dp = [[(-1, ())] * 5 for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = (0, ())
            
        for i in range(1, n + 1):
            l, r, w, orig_id = annotated_intervals[i - 1]
            
            # Find the largest index `prev_idx` where the end time is strictly less than `l`
            # `bisect_left` fetches the first index where elements >= l, so we subtract 1.
            prev_idx = bisect.bisect_left(R, l) - 1
            
            for k in range(1, 5):
                # Option 1: Current interval `i` is excluded
                w1, arr1 = dp[i - 1][k]
                
                # Option 2: Current interval `i` is included
                w_prev, arr_prev = dp[prev_idx][k - 1]
                if w_prev != -1:
                    w2 = w_prev + w
                    arr2 = tuple(sorted(arr_prev + (orig_id,)))
                else:
                    w2 = -1
                    arr2 = ()
                    
                # Store the most optimal track depending on comparisons
                if w2 > w1:
                    dp[i][k] = (w2, arr2)
                elif w2 == w1 and w1 != -1:
                    # In a scenario of matching weights, favor strictly smaller lexicographical sorts
                    if arr2 < arr1:
                        dp[i][k] = (w2, arr2)
                    else:
                        dp[i][k] = (w1, arr1)
                else:
                    dp[i][k] = (w1, arr1)
                    
        # 4. Resolve the overall best answer examining lengths up to 4 parameters
        best_w = -1
        best_arr = ()
        
        for k in range(1, 5):
            w, arr = dp[n][k]
            if w > best_w:
                best_w = w
                best_arr = arr
            elif w == best_w and w != -1:
                if arr < best_arr:
                    best_arr = arr
                    
        return list(best_arr)