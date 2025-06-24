import math
class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        l1 = set()
        for i in range(len(nums)):
            if nums[i] == key:
                for j in range(len(nums)):
                    if abs(j-i)<=k:
                        l1.add(j)
        l1 = sorted(list(l1))
        return l1

        