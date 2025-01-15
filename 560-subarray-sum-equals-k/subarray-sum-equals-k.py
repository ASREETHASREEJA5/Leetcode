class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        c = 0
        mpp = defaultdict(int)
        preSum = 0
        mpp[0]=1
        for i in range(len(nums)):
            preSum+=nums[i]
            rem = preSum-k
            c += mpp[rem]
            mpp[preSum] +=1
        return c