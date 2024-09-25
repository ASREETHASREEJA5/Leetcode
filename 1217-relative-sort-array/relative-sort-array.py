class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        l = []
        for i in arr2:
            print(i)
            a = arr1.count(i)
            for j in range(0,a):
                l.append(i)
                arr1.remove(i)
        arr1.sort()
        return l+arr1
        