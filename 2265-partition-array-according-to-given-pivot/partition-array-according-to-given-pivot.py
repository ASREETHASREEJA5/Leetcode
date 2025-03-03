class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l = []
        m = []
        r = []
        for i in nums:
            if i<pivot:
                l.append(i)
            elif i == pivot:
                m.append(i)
            else:
                r.append(i)
        return l+m+r
        