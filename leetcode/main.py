from typing import List

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        if hasApple.count(False) == n:
            return 0

Solution().minTime()
