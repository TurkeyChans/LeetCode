class Solution:
    # Space O(1)
    # Time O(N)
    def largestAltitude(self, gain: List[int]) -> int:
        i = 1
        ans = 0
        while i < len(gain):
            gain[i] += gain[i-1]
            if gain[i] > ans:
                ans = gain[i]
            i += 1
        return ans if ans > gain[0] else gain[0]
