class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]
        if len(nums) == 1:
            if target in nums:
                return [0,0] 
        l = []
        l.append(nums.index(target))
        for i in range(len(nums)-1,-1,-1):
            if nums[i] == target:
                l.append(i)
                return l