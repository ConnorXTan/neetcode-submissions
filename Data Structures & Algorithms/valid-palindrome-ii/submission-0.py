class Solution:
    def validPalindrome(self, s: str) -> bool:
        s = list(s)
        templist = []
        l, r = 0, len(s) - 1
        if s == s[::-1]:
            return True
        for i in range(len(s)):
            for b in range(len(s)):
                if b != i:
                    templist.append(s[b])
            print(templist)
            if templist == templist[::-1]:
                return True
            templist = []
        return False