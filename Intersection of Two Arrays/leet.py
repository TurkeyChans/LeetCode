from typing import List
# SPACE = O(N + M)
# TIME = O(N + M)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a1 = set(nums1)
        a2 = set(nums2)
        ans = list(a1.intersection(a2))
        return ans
        


            


s1 = Solution()
print(s1.intersection([1,2,2,1],[2,2]))