class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {')': '(', ']': '[', '}': '{'}
        stack = []
        num = len(s)
        for i in range(num):
            if s[i] in pairs:
                if not stack:
                    return False
                if stack.pop() != pairs[s[i]]:
                    return False
                
            else:
                stack.append(s[i])
        return not stack
        
