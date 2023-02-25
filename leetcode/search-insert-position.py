class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
      low = 0
      n = len(nums)
      high = n - 1
      while low <= high:
          mid = int((low + high) / 2)
          if nums[mid] == target:
            return mid
          elif nums[mid] > target: high = mid - 1
          else: low = mid + 1

      return low

print(Solution().searchInsert([-1,3,5,6], 0))
