class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        f, s = 0, 0
        finalstring = ''
        for i in range(len(word1) + len(word2)):
            if f < len(word1):
                finalstring += word1[f]
                f += 1
            if s < len(word2):
                finalstring += word2[s]
                s += 1
        return finalstring