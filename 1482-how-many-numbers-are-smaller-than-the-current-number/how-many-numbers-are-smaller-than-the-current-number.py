class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        nums1 = sorted(nums)
        haset = {}
        for i in range(len(nums1)):
            if nums1[i] not in haset:
                haset[nums1[i]] = i

        return [haset[i] for i in nums]
        