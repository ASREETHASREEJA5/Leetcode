class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        arr.sort()
        arr = arr[::-1]
        for i in range(len(arr)):
            if arr[i]/2 in arr and i != arr.index(arr[i]/2):
                return True
        return False
        