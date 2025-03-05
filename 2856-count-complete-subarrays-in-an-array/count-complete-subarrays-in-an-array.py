class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        c = 0
        x = len(set(nums))
        n = len(nums)
        for i in range(n):
            sub_set = set()
            for j in range(i,n):
                sub_set.add(nums[j])
                if len(sub_set) == x:
                    c+=1
        return c