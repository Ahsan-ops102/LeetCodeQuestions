class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        lines = 1
        current_width = 0
       

        for i in range(len(s)):
            current_letter_width = widths[ord(s[i]) - ord('a')]
            if current_width + current_letter_width <=100:
                current_width += current_letter_width
            else:
                current_width = current_letter_width
                lines+=1
        return [lines, current_width]

