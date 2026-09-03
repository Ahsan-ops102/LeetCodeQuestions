class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        current = []
        i = 0
        current_total = 0

        def recursive(current_index, current_total):
            
            if current_total == target:
                result.append(current.copy())
                return
            elif current_total > target:
                return 
            
            else:
                for i in range(current_index, len(candidates)):
                    current.append(candidates[i])
                    current_total +=candidates[i]
                    recursive(i,current_total)
                    current.pop()
                    current_total -=candidates[i]
        recursive(i, current_total)
        return result

