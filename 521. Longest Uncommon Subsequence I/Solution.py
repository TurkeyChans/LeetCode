#TIME = O(min(N,M))
#Space = O(1)
class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if len(a) != len(b):
            return len(a) if len(a) > len(b) else len(b)
        for i in range(len(a)):
            if a[i] != b[i]:
                return len(a) if len(a) > len(b) else len(b)
        return -1
