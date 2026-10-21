class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        def rev(arr,left,right):
            while left < right:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                right-=1
        n=len(nums)
        k=k%n

        rev(nums,0,n-1)
        rev(nums,0,k-1)
        rev(nums,k,n-1)

        return nums
