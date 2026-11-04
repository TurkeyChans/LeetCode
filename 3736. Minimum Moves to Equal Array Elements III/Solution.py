class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # Time O(N)
        # Space O(1)
        maxs = 0
        j = 0
        ans = 0
        for i in nums:
            if i > maxs:
                maxs = i
        for j in nums:
            if (j != maxs):
                ans += maxs - j
        return ans
