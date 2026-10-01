class Solution:
    def isValid(self, s: str) -> bool:
        # Time O(N)
        # Space O(N)
        arr = []
        size = 0
        for i in s:
            if i == '(' or i == '[' or i == '{':
                arr.append(i)
                size += 1
            else:
                if size != 0:
                    temp = arr.pop()
                    size -= 1
                else:
                    temp = 's'
                if not(((i == ')') and (temp == '(')) or ((i == ']') and (temp == '[')) or ((i == '}') and (temp == '{'))):
                    return False
        return True if size == 0 else False
