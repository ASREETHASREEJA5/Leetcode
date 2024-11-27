class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        max_right = -1  # Initialize with -1 for the last element
        for i in range(n - 1, -1, -1):  # Traverse the array in reverse
            current = arr[i]
            arr[i] = max_right  # Replace current element with the max on the right
            max_right = max(max_right, current)  # Update max_right
        return arr

        