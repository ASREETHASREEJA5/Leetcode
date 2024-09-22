class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        r = len(nums)/3
        l1 = list(set(nums))
        l= []
        for i in l1:
            if nums.count(i)>r:
                l.append(i)
        return l

        