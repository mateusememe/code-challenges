import collections
from typing import List

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        e = collections.defaultdict(list)
        for u, v in edges:
            e[u].append(v)
            e[v].append(u)

        def traverse(node, parent):
            if len(e[node]) == 0:
                return False, 0

            total = 0
            for child in e[node]:
                if child != parent:
                    r, c = traverse(child, node)

                    if r:
                        total += c

            if total > 0 or hasApple[node]:
                return True, total + 2
            else:
                return False, 0

        r, c = traverse(0, -1)
        if r:
            return c - 2

        return 0



Solution().minTime()
