class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        
        result = []
        for row in image:
            

            reversed_row = row[::-1]

            for i in range(len(reversed_row)):
                if reversed_row[i] == 0:
                    reversed_row[i] = 1
                else:
                    reversed_row[i] = 0
            result.append(reversed_row)
        return result