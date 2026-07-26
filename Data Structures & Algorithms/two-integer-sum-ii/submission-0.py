class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            value = target - numbers[i] # 3 - 1 = 2
            left = i + 1
            right = len(numbers) - 1

            while left <= right:
                mid = (left + right) // 2
                if numbers[mid] == value:
                    return [i + 1, mid + 1]
                elif numbers[mid] < value:
                    left = mid + 1
                elif numbers[mid] > value:
                    right = mid - 1
    # Time - O(n * n log n)
    # Space - O(1)
    