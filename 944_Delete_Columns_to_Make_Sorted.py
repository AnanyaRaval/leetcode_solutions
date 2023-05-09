from typing import List

"""
Time Complexity: N * (M + Nlog(N)); N = size of string, M = Number of strings
1. Is there a way we can optimize combining first characters of each string?
2. Is there a way to remove sorting?
"""
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count, N = 0, len(strs[0])
        for i in range(N):
            grid = []
            for s in strs:
                grid.append(s[i])
            if sorted(grid) != grid:
                count += 1
        return count


"""
Removed sorting.
Time Complexity: O(N * M); N = size of string, M = Number of strings
"""
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count, M, N = 0, len(strs), len(strs[0])
        for i in range(N):
            for j in range(1, M):
                if strs[j][i] < strs[j-1][i]:
                    count += 1
                    break
                return count

"""
Used in-built zip function to get first character of each string.
Time Complexity: O(N * M)
"""
class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        return sum([sorted(tup) != list(tup) for tup in zip(*strs)])
       
