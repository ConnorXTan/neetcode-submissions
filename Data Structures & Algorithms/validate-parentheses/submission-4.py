class Solution:
    def isValid(self, s: str) -> bool:
        my_arr = [0]
        if len(s) <= 1:
            return False
        for char in s:
            if char == (')'):
                if my_arr[-1] != '(':
                    return False
                my_arr.pop()
                continue
            if char == (']'):
                if my_arr[-1] != '[':
                    return False
                my_arr.pop()
                continue
            if char == ('}'):
                if my_arr[-1] != '{':
                    return False
                my_arr.pop()
                continue
            my_arr.append(char)
        return my_arr == [0]
            

        