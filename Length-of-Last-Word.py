class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = len(s) - 1

        while s[length] == " ":
            length -=1

        count = 0

        while length != -1 and s[length] != " ":
            length -=1
            count +=1

        return count

