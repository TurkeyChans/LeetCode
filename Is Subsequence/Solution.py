#TIME O(N)
#SPACE O(1)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        count = 0
        k = 0
        if len(s) == 0:
            return True
        for i in range(len(t)):
            
            if s[k] == t[i]:
                k += 1
                count += 1
            if len(s) == count:
                return True
            
        return False
