class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        score = list(enumerate(score))

        score.sort(key=lambda x: x[1], reverse=True)

        answer = [0] * len(score)
       

        for i,j in enumerate(score):
            rank = i+1
            if rank == 1:
                answer[j[0]] = 'Gold Medal'
            elif rank == 2:
                answer[j[0]] = 'Silver Medal'
            elif rank == 3:
                answer[j[0]] = 'Bronze Medal' 
            else:
                answer[j[0]] = str(rank)
        return answer

