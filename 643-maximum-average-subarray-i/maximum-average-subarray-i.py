class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        # sum of first window
        window_sum = sum(nums[:k])
        max_sum = window_sum

        for i in range(k, n):
            window_sum += nums[i] - nums[i-k]  # slide the window
            max_sum = max(max_sum, window_sum)

        return max_sum / k
