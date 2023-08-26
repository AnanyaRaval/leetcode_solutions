# https://leetcode.com/problems/divide-a-string-into-groups-of-size-k/description/

from typing import List

"""
TECHNIQUE: String loop
PROCEDURE:
1. Loop through the string in steps of k and add substring of size k to a result list.
2. If the last substring/last element of the result has len < k:
    2.1 Add fill characters to the last substring to make the length == k.
3. Return result.
TIME COMPLEXITY: O(n)
SPACE COMPLEXITY: O(n + k) #last substring is replaced and uses k extra space.
"""
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        result = []
        for idx in range(0,len(s),k):
            result.append(s[idx:idx+k])
        if len(result[-1]) < k:
            result[-1]+= (fill*(k-len(result[-1])))
        return result

"""
NOTE: Fill elements are required only if len(s) is not exactly divisible by k. 
Check for this and add fill elements to make the length of string divisible by k.

TIME COMPLEXITY: O(2 * n) #Python internally loops over the string to replace it. 
SPACE COMPLEXITY: O(2 * (n+k)) #Strings are immutable in Python. So, takes extra n space when replaced.
"""
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        result = []
        if len(s) % k != 0:
            s += fill * (k - len(s) % k)
        for idx in range(0,len(s),k):
            result.append(s[idx:idx+k])
        return result

"""
NOTE: Is the if condition necesary? We can fill k elements to the string 
        without checking if condition. Run a loop through the string to get substrings 
        of size k. The last substring can start with len(s)-1 at most. In this case, the last characters
        are already filled with fill.

TIME COMPLEXITY: O(2 * n)
SPACE COMPLEXITY: O(2 * (n + k))       
"""
class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        new_s = s + fill * k
        return [new_s[i:i+k] for i in range(0, len(s), k)]
