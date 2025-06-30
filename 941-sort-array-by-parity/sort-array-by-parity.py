class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l = []
        l1 = []
        for i in nums:
            if i%2 == 0:
                l.append(i)
            else:
                l1.append(i)
        return l+l1
        