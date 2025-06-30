class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        l1 = []
        l2 = []
        for i in nums:
            if i%2 == 0:
                l1.append(i)
            else:
                l2.append(i)
        i,j = 0,0
        l = []
        while i<len(l1) or j<len(l2):
            l.append(l1[i])
            l.append(l2[j])
            i+=1
            j+=1
        return l



        