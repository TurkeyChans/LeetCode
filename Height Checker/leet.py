from typing import List
# SPACE = O(n)
# TIME = O(n log n)
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        counts = 0
        sort = heights.copy()
        sort.sort()
        for i in range(len(heights)):
            if not(heights[i] == sort[i]):
                counts += 1
        return counts


            


s1 = Solution()
print(s1.heightChecker([1,2,3,4,5]))