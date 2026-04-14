from typing import List
# SPACE = O(N)
# TIME = O(N^2)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        while i <= len(nums)-1:
            if i != 0:
                if nums[i] == nums[i-1]:
                    nums.pop(i)
                    i -= 1
            i += 1
        return len(nums)

s1 = Solution()
print(s1.removeDuplicates([1,1,1,2,2,3]))
