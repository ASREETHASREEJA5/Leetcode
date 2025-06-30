from collections import Counter

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        if k < 0:
            return 0  # absolute difference can't be negative

        count = 0
        freq = Counter(nums)

        if k == 0:
            # For k = 0, count numbers that appear more than once
            for num in freq:
                if freq[num] > 1:
                    count += 1
        else:
            # For k > 0, check if num + k exists
            for num in freq:
                if num + k in freq:
                    count += 1

        return count
