class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        def encrypt(x):
            l = list(str(x))
            l.sort()
            m = l[-1]
            for i in range(len(l)):
                l[i] = m
            return int("".join(l))
        for i in range(len(nums)):
            nums[i] = encrypt(nums[i])
        return sum(nums)

        
        
        