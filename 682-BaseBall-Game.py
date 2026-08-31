class Solution:
    def calPoints(self, operations: List[str]) -> int:
      
        score = []

        for i in operations:
            if i!= 'D' and i !='+' and i != 'C':
                integer = int(i)
                score.append(integer)
            if i == 'D':
                new_score = score[-1] + score[-1]
                score.append(new_score)
            if i == '+':
                new_score = score[-1] + score[-2]
                score.append(new_score)
            if i == 'C':
                changed_score = score.pop()
                
        return sum(score)