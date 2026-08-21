class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        current_row = [1]
        for i in range(rowIndex):
            new_row = []
            for j in range(1,len(current_row)):
                row = current_row[j-1] + current_row[j]
                new_row.append(row)
                
            new_row.append(1)
            current_row = [1] + new_row    
            
        return current_row
        