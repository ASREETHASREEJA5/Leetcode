class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)//2
        l = list(set(nums))
        for i in l:
            if nums.count(i) > n :
                return i
        