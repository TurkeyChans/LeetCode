class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        #Time O(N log N)
        #Space O(N)
        a = arr.copy()
        a.sort()
        d = dict()
        ans = []
        count = 1
        for j in range(len(a)):
            if a[j] not in d:
                d[a[j]] = count
                count += 1
        for i in range(len(arr)):
            ans.append(d[arr[i]])
        return ans
