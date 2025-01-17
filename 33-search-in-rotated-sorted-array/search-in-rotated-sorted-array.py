class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        i = 0
        j = len(nums)-1
        while(i<=j):
            mid = (j+i)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]>=nums[i]:
                if nums[i]<=target<=nums[mid]:
                    j = mid-1
                else:
                    i = mid+1
            else:
                if nums[mid] <= target <= nums[j]:
                    i = mid + 1
                else:
                    j = mid - 1

        