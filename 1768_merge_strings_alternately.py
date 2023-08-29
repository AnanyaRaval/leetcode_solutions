#https://leetcode.com/problems/merge-strings-alternately/description/

from itertools import zip_longest

"""
TECHNIQUE: TWO POINTERS
PROCEDURE:
1. Initialize 2 pointers ptr1 and ptr2 to point to word1 and word2 resp.
2. Create a while loop which will run till we reach end of both word1 and word2.
    2.1 We add a character of word1 pointed to by ptr1 to the result. Increment ptr1.
    2.2 We add a character of word2 pointed to by ptr2 to the result. Increment ptr2.
    If we reach end of word1 or word2, the loop continues to add characters from the other one.
3. We convert the result list to a string.
TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)
NOTE: Loop invariant: Within every iteration of the while loop, the result will contain the merged
        string characters from [0, ptr1) of word1 and [0, ptr2) of word2.
"""
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        
        ptr1, ptr2, result = 0, 0, []
        LW1, LW2 = len(word1), len(word2)
        while ptr1 < LW1 or ptr2 < LW2:
            result += [word1[ptr1]] if ptr1 < LW1 else ""
            result += [word2[ptr2]] if ptr2 < LW2 else ""
            ptr1 += 1
            ptr2 += 1
        return ''.join(result)

"""
NOTE: Alternate implementation from Leetcode editorial. This adds to the loop invariant:
        ptr1 <= len(word1) and ptr2 <= len(word2) for every iteration.
TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(1)
"""
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ptr1, ptr2, result = 0, 0, []
        LW1, LW2 = len(word1), len(word2)
        while ptr1 < LW1 or ptr2 < LW2:
            if ptr1 < LW1:
                result += word1[ptr1]
                ptr1 += 1
            if ptr2 < LW2:
                result += word2[ptr2]
                ptr2 += 1
        return ''.join(result)

"""
TECHNIQUE: ONE POINTER/FOR LOOP
NOTE: We do not need 2 pointers for both strings. We can run a loop till the max length of both
      strings. We add the characters from both word1 and word2 of the same index for alternating string.
"""
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:   
        n = max(len(word1), len(word2))
        result = []
        for idx in range(n):
            if idx < len(word1):
                result += word1[idx]
            if idx < len(word2):
                result += word2[idx]
        return ''.join(result)

"""
NOTE: Pythonic code (from Discussion section in leetcode.)
"""
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:   
        return ''.join(c for pair in zip_longest(word1, word2, fillvalue='') for c in pair)
        