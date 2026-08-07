class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        

        min_length = [len(word) for word in strs]
        min_length = min(min_length)

        for i in range(min_length):
            letter = strs[0][i]
            for word in strs:
                if word[i] != letter:
                    return strs[0][:i]
        return strs[0][:min_length]