class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #[3, 5, 6, 0, 1, 2]

        l = 0
        r = len(nums) - 1

        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            elif nums[mid] < nums[r]:
                r = mid
            else:
                return mid 
        pivot = l

        left = 0
        right = len(nums) - 1

        if nums[pivot] <= target <= nums[right]:
            left = pivot
        else:
            right = pivot
        
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                return mid
        return -1
            


        

            

                
                

        