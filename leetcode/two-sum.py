class Solution:
    def twoSum(self, nums: list, target: int) -> list:
      _map = {}
      for index in range(len(nums)):
        diff = target - nums[index]

        if diff in _map.keys():
          return [_map.get(diff), index]

        _map[nums[index]] = index

      return [0, 1]
print(Solution().twoSum([3,2,4], 6))
