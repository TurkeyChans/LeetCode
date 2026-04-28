class Solution:
#TIME O(N)
#SPACE O(1)
    def repeatedCharacter(self, s: str) -> str:
        ans = set()
        for i in s:
            if i in ans:
                return i
            else:
                ans.add(i)
