class Solution:
    def findMin(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1
        while low<high:
            mid=(low+high)//2
            if nums[mid-1]>nums[mid]:
                return nums[mid]
            elif nums[mid]>nums[high]:
                low=mid+1
            elif nums[mid]<nums[high]:
                high=mid-1
        return nums[low]