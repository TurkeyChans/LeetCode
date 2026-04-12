from typing import List
import numpy as np
# SPACE = O(N)
# TIME = O(N)
# Note: I know that I can lower down Space O(N) to O(1) by not copying the array. I just wanted to use numpy :).
class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        get_max = max(nums)
        np_nums = np.array(nums)
        x = int(np.where(np_nums == get_max)[0][0])
        nums.remove(get_max)
        np_nums2 = np.array(nums)
        np_double_nums = np_nums2 * 2
        new_nums = list(np_double_nums.tolist())

        for i in range(len(nums)):
            if get_max < new_nums[i]:
                return -1
        return x

            

        
        


s1 = Solution()
print(s1.dominantIndex([1,2,3,4]))
