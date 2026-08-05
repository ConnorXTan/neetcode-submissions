class Solution:
    def isPalindrome(self, s: str) -> bool:
        mystr = ''
        for c in s:
            if c.isalnum():
                mystr += c.lower()
        return (mystr == mystr[::-1])