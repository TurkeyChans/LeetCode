class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        # Time O(N)
        # Space O(N)
        s = set(friends)
        ans = []
        for i in order:
            if i in s:
                ans.append(i)
        return ans
