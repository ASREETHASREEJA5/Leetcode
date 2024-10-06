class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = nums[0]
        for i in range(len(nums)):
            sum1 =0 
            n = str(nums[i])
            for j in n:
                sum1+=int(j) 
            if ans>sum1:
                ans = sum1
        return ans 
        