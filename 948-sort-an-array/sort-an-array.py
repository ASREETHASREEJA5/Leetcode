from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mer(nums):
            if len(nums) > 1:
                mid = len(nums) // 2

                lh = nums[:mid]
                rh = nums[mid:]

                # Recursively sort both halves
                mer(lh)
                mer(rh)

                i = j = k = 0

                # Merge the sorted halves
                while i < len(lh) and j < len(rh):
                    if lh[i] < rh[j]:
                        nums[k] = lh[i]
                        i += 1
                    else:
                        nums[k] = rh[j]
                        j += 1
                    k += 1

                # Handle remaining elements of lh (if any)
                while i < len(lh):
                    nums[k] = lh[i]
                    i += 1
                    k += 1

                # Handle remaining elements of rh (if any)
                while j < len(rh):
                    nums[k] = rh[j]
                    j += 1
                    k += 1

        mer(nums)
        return nums
