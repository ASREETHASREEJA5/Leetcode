class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        l = []
        for i in range(len(nums)):
            a = nums[i]
            l.append(nums[a])
        return l
        