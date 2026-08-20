class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []
        row = 0
        prev = [1]

        for i in range(numRows):
            rows = [1] * (i+1)
            for j in range(1, len(rows)-1):
                row = prev[j-1] + prev[j]
                rows[j] = row
            triangle.append(rows)
            prev = rows
        return triangle
                
   