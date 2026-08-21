class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_string = []
        for i in range(len(s)):
            lowered_case = s[i].lower()
            cleaned = s[i].isalnum()
            if cleaned == True:
                cleaned_string.append(lowered_case)
        
        left = 0
        length = len(cleaned_string)
        right = length - 1
        while(left <= right):
            if cleaned_string[left] == cleaned_string[right]:
                left +=1
                right -=1
            else:
                return False
        return True
