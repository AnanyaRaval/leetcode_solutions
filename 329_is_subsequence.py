# https://leetcode.com/problems/is-subsequence/

"""
TECHNIQUE: Two Pointers
PROCEDURE:
1. Base conditions: If len(s) > len(t), s cannot be a subsequence of t. Return False.
                    If s is empty, it will be a subsequence of any string. Return True
2. Initialize two pointers s_ptr, t_ptr to 0, which point to character in s and t respectively.
3. Start a while loop which loops till the end of either s or t:
    3.1 If char at s[s_ptr] == t[t_ptr], Increment s_ptr.
        This implies we have found 1 character of s in t. We will not find if the next charcter s is in t.
    3.2 Increment t_ptr.
4.  Return if s_ptr == len(s) 
    If s_ptr points to end of s, it means we have enountered all chars of s in t. 

TIME COMPLEXITY: O(T)
SPACE COMPLEXITY: O(1)
NOTE: Loop Invariant: s[0:s_ptr) is a subsequence of t.
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t): return False
        if len(s) == 0: return True

        s_ptr, t_ptr = 0, 0
        while s_ptr < len(s) and t_ptr < len(t):
            if t[t_ptr] == s[s_ptr]:
                s_ptr += 1
            t_ptr += 1
        return s_ptr == len(s)

"""
TECHNIQUE: Two pointers
NOTE: Same procedure as above, with for loop. 
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t): return False
        idx = 0
        for ch in t:
            if idx < len(s) and s[idx] == ch:
                idx += 1
        
        return idx == len(s)

"""
TECHNIQUE: Tail Recursion
PROCEDURE:
1. Create a recurse function which takes s_idx and t_idx as parameters.
    s_idx = index of char being compared in s.
    t_idx = index of char being compared in t.
2. Base conditions to end recurse:
    2.1 If s_idx has reached len(s), all chars in s have been found in t. Return True
    2.2 If t_idx has readed len(t), we have reached end of t but not s. Return False.
3. Recursion condition:
    If s[s_idx] == t[t_idx], recurse with s_idx+1 and t_idx+1.
        This recursion will check if next elem s[s_idx+1] in present in t[t_idx+1:].
    If s[s_idx] != t[t_idx], recurse with s_idx and t_idx+1.
        This recursion will check id curr elem s[s_idx] is present in t[t_idx+1:], since it wasn't found 
        in [0:t_idx].
4. Call this recurse function from beginning of both arrays: s_idx = 0 and t_idx = 0.
TIME COMPLEXITY: O(T)
SPACE COMPLEXITY: O(T) #Will go till end of t in the worst case 
"""
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        def recurse(s_idx:int, t_idx:int) -> bool:
            if s_idx == len(s):
                return True
            if t_idx == len(t):
                return False
            
            if s[s_idx] == t[t_idx]:
                return recurse(s_idx+1, t_idx+1)
            else:
                return recurse(s_idx, t_idx+1)
        return recurse(0,0)


        