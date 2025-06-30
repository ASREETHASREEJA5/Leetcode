class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums)-1
        while(left<right):
            if nums[left]%2 == 0:
                left +=1
            elif nums[right] %2 == 1:
                right-=1
            else:
                nums[left],nums[right] = nums[right],nums[left]
        return nums