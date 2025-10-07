class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMost(k):
            left = 0
            res = 0
            count = 0
            for right in range(len(nums)):
                if nums[right] % 2 != 0:
                    count += 1
                while count > k:
                    if nums[left] % 2 != 0:
                        count -= 1
                    left += 1
                res += right - left + 1
            return res

        return atMost(k) - atMost(k - 1)
