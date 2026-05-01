class Solution:
    #Time O(N)
    #Space O(1)
    def maxDistinct(self, s: str) -> int:
        st = set()
        ans = 0
        for i in s:
            if i not in st:
                st.add(i)
                ans += 1
        return ans
