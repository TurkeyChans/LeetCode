from typing import List

# SPACE = O(1)
# TIME = O(N * M)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.find(needle)
        else:
            return -1


s1 = Solution()
print(s1.strStr("mississippi", "issip"))
