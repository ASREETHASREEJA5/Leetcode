from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        # Step 1: Find two potential candidates
        cand1 = cand2 = None
        cnt1 = cnt2 = 0

        for num in nums:
            if num == cand1:
                cnt1 += 1
            elif num == cand2:
                cnt2 += 1
            elif cnt1 == 0:
                cand1, cnt1 = num, 1
            elif cnt2 == 0:
                cand2, cnt2 = num, 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        # Step 2: Verify actual counts
        res = []
        n = len(nums)
        for c in [cand1, cand2]:
            if c is not None and nums.count(c) > n // 3:
                res.append(c)

        return res
