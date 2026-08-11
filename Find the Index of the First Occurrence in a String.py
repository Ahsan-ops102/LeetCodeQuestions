class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        stop = len(haystack) - len(needle)

        for i in range(stop + 1):
            found = True
            for j in range(0, len(needle)):
               
                if haystack[i+j] != needle[j]:
                    found = False
                    break
                
            if found == True:
                return i
            
        return -1   

