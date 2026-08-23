class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ''
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        while columnNumber > 0:
            columnNumber -=1
            letterIndex = columnNumber % 26
            columnNumber = columnNumber // 26
            result = alphabet[letterIndex] +  result  
        return result