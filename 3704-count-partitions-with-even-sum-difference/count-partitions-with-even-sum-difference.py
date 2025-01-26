class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        n = len(nums)
        c = 0
        for i in range(1,n):
            d = sum(nums[:i])-sum(nums[i:])
            if d % 2 == 0:
                print(nums[:i])
                print(nums[i:])
                c+=1
        return c

        