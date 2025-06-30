class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        totsum = 0
        for i in range(0,len(nums),2):
            totsum+=nums[i]
        return totsum
        