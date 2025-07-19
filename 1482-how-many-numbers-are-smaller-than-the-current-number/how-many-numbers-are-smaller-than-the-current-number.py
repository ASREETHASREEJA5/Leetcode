class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums1 = nums.copy()
        nums1.sort()
        for i in range(len(nums)):
            nums[i] = nums1.index(nums[i])
        return nums
        