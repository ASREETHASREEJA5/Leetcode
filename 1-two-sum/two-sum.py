class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l = []
        for i in range(len(nums)):
            if target-nums[i] in nums[i+1:]:
                l1 = nums[i+1:]
                l.append(i)
                l.append(l1.index(target-nums[i])+i+1)
                return l

        